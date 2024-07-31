# flake8: noqa: E501
from typing import List


def keys_with_max_value(d):
    """
    Find keys with the maximum value in a dictionary.

    Args:
        d (dict): The input dictionary.

    Returns:
        List: A list of keys that correspond to the maximum value in the dictionary.
    """
    max_value = max(d.values())
    max_keys = [k for k, v in d.items() if v == max_value]
    return max_keys


def remove_duplicate_keep_first(
    word_list: List[str], duplicate_word: List[str]
) -> List[str]:
    """
    Remove duplicates from a list of words, keeping the first occurrence of each word.

    Args:
        word_list (List[str]): The input list of words.
        duplicate_word (List[str]): A list of words to check for duplicates.

    Returns:
        List[str]: A new list with duplicates removed, keeping the first occurrence.
    """
    unique_list = []
    duplicate_word = set(duplicate_word)
    for word in word_list:
        if word not in duplicate_word:
            unique_list.append(word)
        elif word in unique_list:
            continue
        else:
            unique_list.append(word)
    return unique_list


def remove_longest_repeating_words(word_list: List[str]) -> List[str]:
    """
    Remove words that repeat more than 3 times in the input list.

    Args:
        word_list (List[str]): The input list of words.

    Returns:
        List[str]: A new list with words repeating more than 3 times removed.
    """
    if len(set(word_list)) == len(word_list):
        return word_list

    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    print(word_count)
    repeat_words = [wd for wd, cnt in word_count.items() if cnt > 3]
    if repeat_words:
        print(f"repeating words = {repeat_words}")
        return remove_duplicate_keep_first(word_list, repeat_words)
    else:
        return word_list
