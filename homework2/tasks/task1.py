"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document

"""
from string import punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Finds 10 longest words consisting from largest amount of unique symbols.

    Args:
        file_path: Path to file.

    Returns:
        List of words.

    """

    def find_a_word():
        """Finds a word.

        Returns:
            A word.

        """
        for word in data:
            local_num_of_unique_char = {}
            local_word = ""
            for sym in word + ",":
                if sym not in excluded_punctuation:
                    local_word += sym
                    if sym not in local_num_of_unique_char:
                        local_num_of_unique_char[sym] = 1
                else:
                    yield local_word, local_num_of_unique_char
                    local_num_of_unique_char = {}
                    local_word = ""

    with open(file_path, encoding="unicode-escape") as data:
        data = data.read().split()

    excluded_punctuation = {i for i in punctuation}

    longest_words = []
    gen = find_a_word()
    for _ in range(10):
        longest_words.append(next(gen))

    for a_word in gen:
        for ind in range(10):
            if len(a_word[1]) > len(longest_words[ind][1]):
                longest_words[ind], a_word = a_word, longest_words[ind]

    return [i[0] for i in longest_words]


def get_rarest_char(file_path: str) -> str:
    """Finds the rarest symbol for the document.

    Args:
        file_path: Path to file.

    Returns:
        The rarest symbol.

    """
    with open(file_path, encoding="unicode-escape") as data:
        data = data.read()

    symbols = {}
    for sym in data:
        if sym not in symbols:
            symbols[sym] = 1
        else:
            symbols[sym] += 1

    the_rarest_symbol = min(symbols.items(), key=lambda x: x[1])[0]

    return the_rarest_symbol


def count_punctuation_chars(file_path: str) -> int:
    """Counts each punctuation mark.

    Args:
        file_path: Path to file.

    Returns:
        Num of punctuation marks.

    """
    with open(file_path, encoding="unicode-escape") as data:
        dictionary_of_punc_marks = {i for i in punctuation}
        counter = 0
        for word in data.read().split():
            for sym in word:
                if sym in dictionary_of_punc_marks:
                    counter += 1

    return counter


def count_non_ascii_chars(file_path: str) -> int:
    """Counts non-ascii characters.

    Args:
        file_path: Path to file.

    Returns:
        The number of non-ascii characters.

    """
    with open(file_path, encoding="unicode-escape") as data:
        data = data.read()
        counter = 0
        for sym in data:
            if not (0 <= ord(sym) <= 127):
                counter += 1

    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Finds the most common non-ascii characters.

    Args:
        file_path: Path to file.

    Returns:
        The most common non-ascii character.

    """
    with open(file_path, encoding="unicode-escape") as data:
        data = data.read()

    non_ascii_characters = {}

    for sym in data:
        if not (0 <= ord(sym) <= 127):
            if sym not in non_ascii_characters:
                non_ascii_characters[sym] = 1
            else:
                non_ascii_characters[sym] += 1

    char = ""
    quantity = float("-inf")
    for sym in non_ascii_characters:
        if non_ascii_characters[sym] > quantity:
            char = sym
            quantity = non_ascii_characters[sym]

    return char
