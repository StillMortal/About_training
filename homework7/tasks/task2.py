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


def getting_rid_of_backspaces(string: str) -> str:
    """Uses backspaces to remove the corresponding characters.

    Args:
        string: A string with backspaces.

    Returns:
        String after using backspaces.

    """

    num_of_backspaces = 0
    list_of_characters_without_backspaces = []
    for char in reversed(string):
        if char == "#":
            num_of_backspaces += 1
        elif num_of_backspaces == 0:
            list_of_characters_without_backspaces.append(char)
        else:
            num_of_backspaces -= 1

    return "".join(list_of_characters_without_backspaces)


def backspace_compare(first: str, second: str):
    """Checks whether two strings are equal after using backspaces.

    Args:
        first: First string to check.
        second: Second string to check.

    Returns:
        True if successful, False otherwise.

    """

    return getting_rid_of_backspaces(first) == getting_rid_of_backspaces(second)
