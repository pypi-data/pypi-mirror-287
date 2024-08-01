"""
Cleaners are transformations that run over the input text at both training and eval time.
Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You'll typically want to use:
  1. "english_cleaners" for English text
  2. "transliteration_cleaners" for non-English text that can be transliterated to ASCII using
     the Unidecode library (https://pypi.python.org/pypi/Unidecode)
  3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
     the symbols in symbols.py to match your data).
"""
import logging
import re

from phonemizer import phonemize
from phonemizer.backend import EspeakBackend

# To avoid excessive logging we set the log level of the phonemizer package to Critical
critical_logger = logging.getLogger("phonemizer")
critical_logger.setLevel(logging.CRITICAL)

backend_cat = None
backend_bal = None
backend_val = None
backend_occ = None

# Regular expression matching whitespace:
_whitespace_re = re.compile(r"\s+")

# List of (regular expression, replacement) pairs for abbreviations:
_abbreviations = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("mrs", "misess"),
        ("mr", "mister"),
        ("dr", "doctor"),
        ("st", "saint"),
        ("co", "company"),
        ("jr", "junior"),
        ("maj", "major"),
        ("gen", "general"),
        ("drs", "doctors"),
        ("rev", "reverend"),
        ("lt", "lieutenant"),
        ("hon", "honorable"),
        ("sgt", "sergeant"),
        ("capt", "captain"),
        ("esq", "esquire"),
        ("ltd", "limited"),
        ("col", "colonel"),
        ("ft", "fort"),
    ]
]


def expand_abbreviations(text):
    for regex, replacement in _abbreviations:
        text = re.sub(regex, replacement, text)
    return text


def lowercase(text):
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, " ", text)


def convert_to_ascii(text):
    from unidecode import unidecode
    return unidecode(text)


def basic_cleaners(text):
    """Basic pipeline that lowercases and collapses whitespace without transliteration."""
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def transliteration_cleaners(text):
    """Pipeline for non-English text that transliterates to ASCII."""
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def english_cleaners(text):
    """Pipeline for English text, including abbreviation expansion."""
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = expand_abbreviations(text)
    phonemes = phonemize(text, language="en-us", backend="espeak", strip=True)
    phonemes = collapse_whitespace(phonemes)
    return phonemes


def english_cleaners2(text):
    """Pipeline for English text, including abbreviation expansion. + punctuation + stress"""
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = expand_abbreviations(text)
    phonemes = phonemize(
        text,
        language="en-us",
        backend="espeak",
        strip=True,
        preserve_punctuation=True,
        with_stress=True,
    )
    phonemes = collapse_whitespace(phonemes)
    return phonemes


def catalan_cleaners(text):
    """Pipeline for catalan text, including punctuation + stress"""
    global backend_cat
    if backend_cat is None:
        # lazy loaded
        backend_cat = EspeakBackend("ca", preserve_punctuation=True, with_stress=True)
    # text = convert_to_ascii(text)
    text = lowercase(text)
    # text = expand_abbreviations(text)
    phonemes = backend_cat.phonemize([text], strip=True)[0]
    phonemes = collapse_whitespace(phonemes)
    return phonemes


def catalan_balear_cleaners(text):
    """Pipeline for Catalan text, including abbreviation expansion. + punctuation + stress"""
    global backend_bal
    if backend_bal is None:
        backend_bal = EspeakBackend("ca-ba", preserve_punctuation=True, with_stress=True)
    # text = convert_to_ascii(text)
    text = lowercase(text)
    # text = expand_abbreviations(text)
    phonemes = backend_bal.phonemize([text], strip=True, njobs=1)[0]
    phonemes = collapse_whitespace(phonemes)
    # print(phonemes)  # check punctuations!!
    return phonemes


def catalan_occidental_cleaners(text):
    """Pipeline for Catalan text, including abbreviation expansion. + punctuation + stress"""
    global backend_occ
    if backend_occ is None:
        backend_occ = EspeakBackend("ca-nw", preserve_punctuation=True, with_stress=True)
    # text = convert_to_ascii(text)
    text = lowercase(text)
    # text = expand_abbreviations(text)
    phonemes = backend_occ.phonemize([text], strip=True, njobs=1)[0]
    phonemes = collapse_whitespace(phonemes)
    # print(phonemes)  # check punctuations!!
    return phonemes


def catalan_valencia_cleaners(text):
    """Pipeline for Catalan text, including abbreviation expansion. + punctuation + stress"""
    global backend_val
    if backend_val is None:
        backend_val = EspeakBackend("ca-va", preserve_punctuation=True, with_stress=True)
    # text = convert_to_ascii(text)
    text = lowercase(text)
    # text = expand_abbreviations(text)
    phonemes = backend_val.phonemize([text], strip=True, njobs=1)[0]
    phonemes = collapse_whitespace(phonemes)
    # print(phonemes)  # check punctuations!!
    return phonemes
