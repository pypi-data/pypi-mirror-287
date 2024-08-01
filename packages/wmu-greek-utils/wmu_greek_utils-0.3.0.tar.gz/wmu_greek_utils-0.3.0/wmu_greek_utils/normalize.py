import unicodedata
from greek_normalisation.utils import strip_accents as tauber_remove_accents
from greek_normalisation.regexes import GRC_CHAR

from enum import Flag, auto

import regex as re

GREEK_LETTER_PATTERN = re.compile(GRC_CHAR)


def is_greek_letter(char):
    return GREEK_LETTER_PATTERN.match(char)


def is_letter(char):
    return char.isalpha()


def iota_subscript_to_iota_adscript(text):
    IOTA_ADSCRIPT_BYTES = b"\xce\xb9"  # UTF-8 bytes for 'ι'
    IOTA_SUBSCRIPT_BYTES = b"\xcd\x85"  # UTF-8 bytes for the iota subscript character

    # Normalize the text to NFD form
    nfd_text = unicodedata.normalize("NFD", text)

    # Convert the normalized text to bytes
    nfd_bytes = nfd_text.encode("utf-8")

    # Replace the iota subscript bytes with iota adscript bytes
    replaced_bytes = nfd_bytes.replace(IOTA_SUBSCRIPT_BYTES, IOTA_ADSCRIPT_BYTES)

    # Convert the bytes back to a string
    new_text = replaced_bytes.decode("utf-8")

    # Normalize the resulting text back to NFC form
    return unicodedata.normalize("NFC", new_text)


def remove_breathiing(text):
    SMOOTH_BREATHING_BYTES = b"\xcc\x93"
    ROUGH_BREATHING_BYTES = b"\xcc\x94"
    # Normalize the text to NFD form
    nfd_text = unicodedata.normalize("NFD", text)

    # Convert the normalized text to bytes
    nfd_bytes = nfd_text.encode("utf-8")

    # Replace the breathing bytes with an empty byte
    replaced_bytes = nfd_bytes.replace(SMOOTH_BREATHING_BYTES, b"").replace(
        ROUGH_BREATHING_BYTES, b""
    )
    # Convert the bytes back to a string
    new_text = replaced_bytes.decode("utf-8")
    # Normalize the resulting text back to NFC form
    return unicodedata.normalize("NFC", new_text)


def remove_punctuation(text):
    return re.sub(r"\p{P}+", "", text)


class NormalizationOptions(Flag):
    UNCHANGED = 0
    LOWERCASE = auto()
    UPPERCASE = auto()
    REMOVE_SPACES = auto()
    REMOVE_NEWLINES = auto()
    REMOVE_PUNCTUATION = auto()
    REMOVE_ACCENTS = auto()
    REMOVE_BREATHING = auto()
    IOTA_ADSCRIPT = auto()
    NORMALIZE_SIGMA = auto()
    NORMALIZE_THETA = auto()
    NORMALIZE_PHI = auto()
    NORMALIZE_APOSTROPHE = auto()
    ALL = (
        UPPERCASE
        | REMOVE_SPACES
        | REMOVE_NEWLINES
        | REMOVE_PUNCTUATION
        | REMOVE_ACCENTS
        | REMOVE_BREATHING
        | IOTA_ADSCRIPT
        | NORMALIZE_SIGMA
        | NORMALIZE_THETA
        | NORMALIZE_PHI
        | NORMALIZE_APOSTROPHE
    )

    STANDARD = LOWERCASE | NORMALIZE_THETA | NORMALIZE_PHI | NORMALIZE_APOSTROPHE

    SEARCH_STANDARD = (
        LOWERCASE
        | REMOVE_BREATHING
        | REMOVE_ACCENTS
        | IOTA_ADSCRIPT
        | NORMALIZE_SIGMA
        | NORMALIZE_THETA
        | NORMALIZE_PHI
        | NORMALIZE_APOSTROPHE
    )


class Normalizer:
    def __init__(
        self,
        config=NormalizationOptions.STANDARD,
    ):
        self.config = config

    def normalize_case(self, text):
        if self.config & NormalizationOptions.LOWERCASE:
            return text.lower()
        if self.config & NormalizationOptions.UPPERCASE:
            return text.upper()
        return text

    def normalize_spaces(self, text):
        if self.config & NormalizationOptions.REMOVE_SPACES:
            return text.replace(" ", "")
        return text

    def normalize_newlines(self, text):
        if self.config & NormalizationOptions.REMOVE_NEWLINES:
            return text.replace("\n", "")
        return text

    def normalize_breathing(self, text):
        if self.config & NormalizationOptions.REMOVE_BREATHING:
            return remove_breathiing(text)
        return text

    def normalize_accents(self, text):
        if self.config & NormalizationOptions.REMOVE_ACCENTS:
            return tauber_remove_accents(text)
        return text

    def normalize_punctuation(self, text):
        if self.config & NormalizationOptions.REMOVE_PUNCTUATION:
            return remove_punctuation(text)
        return text

    def normalize_iota_subscripts(self, text):
        if self.config & NormalizationOptions.IOTA_ADSCRIPT:
            return iota_subscript_to_iota_adscript(text)
        return text

    def normalize_sigmas(self, text):
        if self.config & NormalizationOptions.NORMALIZE_SIGMA:
            t1 = re.sub(r"[σςϲ]", "ϲ", text)
            t2 = re.sub(r"[ΣϹ]", "Ϲ", t1)
            return t2
        return text

    def normalize_thetas(self, text):
        if self.config & NormalizationOptions.NORMALIZE_THETA:
            t1 = re.sub(r"[θϑ]", "θ", text)
            t2 = re.sub(r"[Θϴ]", "Θ", t1)
            return t2
        return text

    def normalize_phis(self, text):
        if self.config & NormalizationOptions.NORMALIZE_PHI:
            return re.sub(r"[φϕ]", "φ", text)
        return text

    def normalize_apostrophes(self, text):
        if self.config & NormalizationOptions.NORMALIZE_APOSTROPHE:
            # \u02bc is the modifier letter apostrophe
            # \u2019 is the right single quotation mark
            return text.replace("\u2019", "'").replace("\u02bc", "'")
        return text

    def normalize(self, text):
        text = self.normalize_case(text)
        text = self.normalize_spaces(text)
        text = self.normalize_newlines(text)
        text = self.normalize_breathing(text)
        text = self.normalize_accents(text)
        text = self.normalize_punctuation(text)
        text = self.normalize_iota_subscripts(text)
        text = self.normalize_sigmas(text)
        text = self.normalize_thetas(text)
        text = self.normalize_phis(text)
        text = self.normalize_apostrophes(text)
        return text

    def normalise(self, text):
        return self.normalize(text)

    def __call__(self, text):
        return self.normalize(text)
