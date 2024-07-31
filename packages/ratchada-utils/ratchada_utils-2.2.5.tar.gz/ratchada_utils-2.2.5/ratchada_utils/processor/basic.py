# flake8: noqa: E501
import re
import unicodedata

import regex

# non-ASCII letters that are not separated by "NFKD" normalization
ADDITIONAL_DIACRITICS = {
    "œ": "oe",
    "Œ": "OE",
    "ø": "o",
    "Ø": "O",
    "æ": "ae",
    "Æ": "AE",
    "ß": "ss",
    "ẞ": "SS",
    "đ": "d",
    "Đ": "D",
    "ð": "d",
    "Ð": "D",
    "þ": "th",
    "Þ": "th",
    "ł": "l",
    "Ł": "L",
}


def remove_symbols_and_diacritics(s: str, keep=""):
    """
    Remove symbols, punctuations, and diacritics from a string.

    Args:
        s (str): The input string to process.
        keep (str, optional): Characters to keep in the string. Defaults to "".

    Returns:
        str: The processed string with symbols, punctuations, and diacritics removed.
    """
    return "".join(
        (
            c
            if c in keep
            else (
                ADDITIONAL_DIACRITICS[c]
                if c in ADDITIONAL_DIACRITICS
                else (
                    ""
                    if unicodedata.category(c) == "Mn"
                    else " "
                    if unicodedata.category(c)[0] in "MSP"
                    else c
                )
            )
        )
        for c in unicodedata.normalize("NFKD", s)
    )


def remove_symbols(s: str):
    """
    Remove symbols and punctuations from a string, keeping diacritics.

    Args:
        s (str): The input string to process.

    Returns:
        str: The processed string with symbols and punctuations removed.
    """
    return "".join(
        " " if unicodedata.category(c)[0] in "MSP" else c
        for c in unicodedata.normalize("NFKC", s)
    )


class BasicTextNormalizer:
    """
    A class for basic text normalization.

    Args:
        remove_diacritics (bool, optional): Whether to remove diacritics. Defaults to False.
        split_letters (bool, optional): Whether to split letters. Defaults to False.
    """

    def __init__(self, remove_diacritics: bool = False, split_letters: bool = False):
        self.clean = (
            remove_symbols_and_diacritics if remove_diacritics else remove_symbols
        )
        self.split_letters = split_letters

    def __call__(self, s: str):
        """
        Normalize the input text.

        Args:
            s (str): The input string to normalize.

        Returns:
            str: The normalized string.
        """
        s = s.lower()
        s = re.sub(r"[<\[][^>\]]*[>\]]", "", s)  # remove words between brackets
        s = re.sub(r"\(([^)]+?)\)", "", s)  # remove words between parenthesis
        s = self.clean(s).lower()

        if self.split_letters:
            s = " ".join(regex.findall(r"\X", s, regex.U))

        s = re.sub(
            r"\s+", " ", s
        )  # replace any successive whitespace characters with a space

        return s
