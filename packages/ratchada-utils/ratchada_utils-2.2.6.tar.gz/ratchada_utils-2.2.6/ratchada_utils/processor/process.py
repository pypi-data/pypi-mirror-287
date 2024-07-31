# flake8: noqa: E722
import re
from typing import List

import deepcut
from langdetect import detect

from .english import EnglishTextNormalizer
from .postfix import remove_longest_repeating_words


def en_preprocess(text: str) -> str:
    """
    Preprocess English text by removing specific patterns.

    Args:
        text (str): The input English text to preprocess.

    Returns:
        str: The preprocessed English text.
    """
    text = re.sub("[QA]:|(uh)", "", text)
    return text


def th_preprocess(text: str) -> str:
    """
    Preprocess Thai text by removing specific patterns.

    Args:
        text (str): The input Thai text to preprocess.

    Returns:
        str: The preprocessed Thai text.
    """
    text = re.sub("((ค่ะ)|((นะ)?ครับ)|(นะคะ)|เอ่อ)+", "", text)
    return text


def pred_postprocess(listtext: List[str]) -> List[str]:
    """
    Postprocess a list of text tokens by removing spaces and repeating words.

    Args:
        listtext (List[str]): A list of text tokens to postprocess.

    Returns:
        List[str]: The postprocessed list of text tokens.
    """
    if " " in listtext:
        listtext.remove(" ")

    clean_text = remove_longest_repeating_words(listtext)  # changed
    return clean_text


def tokenize_text(text: str, pred=False) -> list:
    """
    Tokenize input text based on detected language and apply preprocessing and postprocessing.

    Args:
        text (str): The input text to tokenize.
        pred (bool, optional): Whether to apply postprocessing. Defaults to False.

    Returns:
        List[str]: A list of tokenized words from the input text.
    """
    if not isinstance(text, str):
        return []
    try:
        lang = detect(text)
    except:
        lang = "en"
    if lang != "en":
        text = th_preprocess(text)
        splited_text = deepcut.tokenize(text)
    else:
        eng_normalizer = EnglishTextNormalizer()
        text = eng_normalizer(text)
        text = en_preprocess(text)
        splited_text = text.split(" ")

    return pred_postprocess(splited_text) if pred else splited_text
