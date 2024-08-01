import os.path

import onnxruntime
import yaml
from ovos_plugin_manager.templates.tts import TTS
from phonemizer.backend import EspeakBackend

from ovos_tts_plugin_matxa_multispeaker_cat.tts import get_tts, DEFAULT_ACCENT, DEFAULT_SPEAKER_ID


class MatxaCatalanTTSPlugin(TTS):
    """Interface to matxaCatalanTTSPlugin."""

    def __init__(self, lang="ca-es", config=None):
        super(MatxaCatalanTTSPlugin, self).__init__(lang=lang, config=config, audio_ext='wav')
        bin_file = self.config.get("espeak_bin", "/usr/local/lib/libespeak-ng.so")
        if not os.path.isfile(bin_file):
            raise FileNotFoundError("please follow instructions to install the catalan espeak fork\n"
                                    "   git clone https://github.com/projecte-aina/espeak-ng\n"
                                    "   cd ./espeak-ng\n"
                                    "   ./autogen.sh\n"
                                    "   ./configure\n"
                                    "   make\n"
                                    "   sudo make install\n"
                                    "the file '/usr/local/lib/libespeak-ng.so' should be created if the install succeeds")
        EspeakBackend.set_library(bin_file)

        MODEL_PATH_matxa_MEL_ALL = f"{os.path.dirname(__file__)}/matcha_multispeaker_cat_all_opset_15_10_steps.onnx"
        MODEL_PATH_VOCOS = f"{os.path.dirname(__file__)}/mel_spec_22khz_cat.onnx"
        VOCODER_CONFIG_PATH = f"{os.path.dirname(__file__)}/config.yaml"

        with open(VOCODER_CONFIG_PATH, "r") as f:
            self.vocoder_config = yaml.safe_load(f)

        # Load models
        sess_options = onnxruntime.SessionOptions()

        self.matxa_mel_all = onnxruntime.InferenceSession(MODEL_PATH_matxa_MEL_ALL,
                                                           sess_options=sess_options,
                                                           providers=["CPUExecutionProvider"])
        self.vocos = onnxruntime.InferenceSession(MODEL_PATH_VOCOS,
                                                  sess_options=sess_options,
                                                  providers=["CPUExecutionProvider"])

    def get_tts(self, sentence, wav_file, lang=None, voice=None):
        """Generate WAV and phonemes.

        Arguments:
            sentence (str): sentence to generate audio for
            wav_file (str): output file
            lang (str): optional lang override
            voice (str): optional voice override

        Returns:
            tuple ((str) file location, (str) generated phonemes)
        """
        voice = voice or self.voice
        lang = lang or self.lang
        if not voice or voice == "default":
            if lang == "ca-ba":
                voice = "balear/quim"
            elif lang == "ca-nw":
                voice =  "nord-occidental/pere"
            elif lang == "ca-va":
                voice =  "valencia/lluc"
            else:
                voice = "central/grau"

        accent, speaker = voice.split("/")
        get_tts(sentence, wav_file,
                model_matxa_mel=self.matxa_mel_all,
                model_vocos=self.vocos,
                accent=accent,
                spk_name=speaker,
                vocoder_config=self.vocoder_config)
        return wav_file, None

    @property
    def available_languages(self) -> set:
        """Return languages supported by this TTS implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return {"ca-es", "ca-nw", "ca-ba", "ca-va"}


if __name__ == "__main__":
    sent = "Això és una prova de síntesi de veu."
    t = MatxaCatalanTTSPlugin()
    t.get_tts(sent, "test.wav", voice="valencia/gina")
