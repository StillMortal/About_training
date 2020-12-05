"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest


def getting_rid_of_backspaces(string: str) -> str:
    """Uses backspaces to remove the corresponding characters.

    Args:
        string: A string with backspaces.

    Returns:
        Generator.

    """

    num_of_backspaces = 0
    for char in reversed(string):
        if char == "#":
            num_of_backspaces += 1
        elif num_of_backspaces == 0:
            yield char
        else:
            num_of_backspaces -= 1


def backspace_compare(first: str, second: str):
    """Checks whether two strings are equal after using backspaces.

    Args:
        first: First string to check.
        second: Second string to check.

    Returns:
        True if successful, False otherwise.

    """

    for char_of_the_first, char_of_the_second in zip_longest(
        getting_rid_of_backspaces(first), getting_rid_of_backspaces(second)
    ):
        if char_of_the_first != char_of_the_second:
            return False
    return True
