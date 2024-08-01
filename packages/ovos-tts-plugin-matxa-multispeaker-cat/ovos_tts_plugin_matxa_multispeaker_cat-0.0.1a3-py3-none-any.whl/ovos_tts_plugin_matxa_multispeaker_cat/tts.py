from time import perf_counter

import numpy as np
import onnxruntime
import soundfile as sf
from scipy.fft import irfft
from scipy.signal.windows import hann

from ovos_tts_plugin_matxa_multispeaker_cat.text import text_to_sequence, sequence_to_text

DEFAULT_SPEAKER_ID = "quim"
DEFAULT_ACCENT = "balear"

speaker_id_dict = {
    "balear": {
        "quim": 0,
        "olga": 1
    },
    "central": {
        "grau": 2,
        "elia": 3
    },
    "nord-occidental": {
        "pere": 4,
        "emma": 5
    },
    "valencia": {
        "lluc": 6,
        "gina": 7
    }
}

cleaners = {"balear": "catalan_balear_cleaners",
            "nord-occidental": "catalan_occidental_cleaners",
            "valencia": "catalan_valencia_cleaners",
            "central": "catalan_cleaners"}


def intersperse(lst, item):
    result = [item] * (len(lst) * 2 + 1)
    result[1::2] = lst
    return result


def process_text(i: int, text: str, cleaner: str):
    print(f"[{i}] - Input text: {text}")
    # Convert text to sequence and intersperse with 0
    text_sequence = text_to_sequence(text, [cleaner])
    interspersed_sequence = intersperse(text_sequence, 0)

    # Convert to NumPy array
    x = np.array(interspersed_sequence, dtype=np.int64)[None]
    x_lengths = np.array([x.shape[-1]], dtype=np.int64)
    x_phones = sequence_to_text(x.squeeze(0).tolist())

    print(x_phones)
    return x, x_lengths


def vocos_inference(mel, denoise, model_vocos, config=None):
    config = config or {
        'backbone': {'class_path': 'vocos.models.VocosBackbone',
                     'init_args': {'dim': 512, 'input_channels': 80, 'intermediate_dim': 1536, 'num_layers': 8}},
        'feature_extractor': {'class_path': 'vocos.feature_extractors.MelSpectrogramFeatures',
                              'init_args': {'f_max': 8000, 'f_min': 0, 'hop_length': 256, 'mel_scale': 'slaney',
                                            'n_fft': 1024, 'n_mels': 80, 'norm': 'slaney', 'padding': 'same',
                                            'sample_rate': 22050}},
        'head': {'class_path': 'vocos.heads.ISTFTHead',
                 'init_args': {'dim': 512, 'hop_length': 256, 'n_fft': 1024, 'padding': 'same'}}
    }

    params = config["feature_extractor"]["init_args"]
    sample_rate = params["sample_rate"]
    n_fft = params["n_fft"]
    hop_length = params["hop_length"]
    win_length = n_fft

    # ONNX inference
    mag, x, y = model_vocos.run(None, {"mels": mel})

    # Complex spectrogram from vocos output
    spectrogram = mag * (x + 1j * y)
    window = hann(win_length, sym=False)

    if denoise:
        # Vocoder bias
        mel_rand = np.zeros_like(mel)
        mag_bias, x_bias, y_bias = model_vocos.run(
            None,
            {
                "mels": mel_rand.astype(np.float32)
            },
        )

        # Complex spectrogram from vocos output
        spectrogram_bias = mag_bias * (x_bias + 1j * y_bias)

        # Denoising
        spec = np.stack([np.real(spectrogram), np.imag(spectrogram)], axis=-1)
        # Get magnitude of vocos spectrogram
        mag_spec = np.sqrt(np.sum(spec ** 2, axis=-1))

        # Get magnitude of bias spectrogram
        spec_bias = np.stack([np.real(spectrogram_bias), np.imag(spectrogram_bias)], axis=-1)
        mag_spec_bias = np.sqrt(np.sum(spec_bias ** 2, axis=-1))

        # Subtract
        strength = 0.0025
        mag_spec_denoised = mag_spec - mag_spec_bias * strength
        mag_spec_denoised = np.clip(mag_spec_denoised, 0.0, None)

        # Return to complex spectrogram from magnitude
        angle = np.arctan2(np.imag(spectrogram), np.real(spectrogram))
        spectrogram = mag_spec_denoised * (np.cos(angle) + 1j * np.sin(angle))

    # Inverse STFT
    pad = (win_length - hop_length) // 2
    B, N, T = spectrogram.shape

    print("Spectrogram synthesized shape", spectrogram.shape)

    # Inverse FFT
    ifft = irfft(spectrogram, n=n_fft, axis=1)
    ifft *= window[None, :, None]

    # Overlap and Add
    output_size = (T - 1) * hop_length + win_length
    y = np.zeros((B, output_size))
    for b in range(B):
        for t in range(T):
            y[b, t * hop_length:t * hop_length + win_length] += ifft[b, :, t]

    # Window envelope
    window_sq = np.expand_dims(window ** 2, axis=0)
    window_envelope = np.zeros((B, output_size))
    for b in range(B):
        for t in range(T):
            window_envelope[b, t * hop_length:t * hop_length + win_length] += window_sq[0]

    # Debugging information
    print("Min window envelope value:", np.min(window_envelope))
    print("Max window envelope value:", np.max(window_envelope))
    print("Min y value:", np.min(y))
    print("Max y value:", np.max(y))

    # Normalize
    if np.any(window_envelope <= 1e-11):
        print("Warning: Some window envelope values are very small.")

    y /= np.maximum(window_envelope, 1e-11)  # Prevent division by very small values

    return y


def get_tts(text: str,
            output_file: str,
            model_matxa_mel: onnxruntime.InferenceSession,
            model_vocos: onnxruntime.InferenceSession,
            accent: str = DEFAULT_ACCENT,
            spk_name: str = DEFAULT_SPEAKER_ID,
            temperature: float = 0.667,
            length_scale: float = 1.0,
            vocoder_config=None):

    if len(text) > 500:
        # TODO - chunk
        print("The maximum input allowed is 500 characters.")
        raise ValueError("The maximum input allowed is 500 characters.")

    else:
        denoise = True
        spk_id = speaker_id_dict[accent][spk_name]
        sid = np.array([int(spk_id)]) if spk_id is not None else None
        text_matxa, text_lengths = process_text(0, text, cleaner=cleaners[accent])

        # matxa VOCOS
        inputs = {
            "x": text_matxa,
            "x_lengths": text_lengths,
            "scales": np.array([temperature, length_scale], dtype=np.float32),
            "spks": sid
        }
        mel_t0 = perf_counter()
        # matxa mel inference
        mel, mel_lengths = model_matxa_mel.run(None, inputs)
        mel_infer_secs = perf_counter() - mel_t0
        print("matxa Mel inference time", mel_infer_secs)

        vocos_t0 = perf_counter()
        # vocos inference
        wavs_vocos = vocos_inference(mel, denoise,
                                     model_vocos=model_vocos,
                                     config=vocoder_config)
        vocos_infer_secs = perf_counter() - vocos_t0
        print("Vocos inference time", vocos_infer_secs)

        with open(output_file, "wb") as fp_matxa_vocos:
            sf.write(output_file, wavs_vocos.squeeze(0), 22050, "PCM_24")

        print(f"RTF matxa + vocos {(mel_infer_secs + vocos_infer_secs) / (wavs_vocos.shape[1] / 22050)}")
        return output_file
