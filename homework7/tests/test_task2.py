import pytest

from homework7.tasks.task2 import backspace_compare


@pytest.mark.parametrize(
    ["first_string", "second_string", "expected_result"],
    [
        ("", "", True),
        ("", "###", True),
        ("ab#c", "ad#c", True),
        ("a#b#", "c#d#", True),
        ("#a#b", "#e#b", True),
        ("ab##", "ed##", True),
        ("abc##", "aed##", True),
        ("abc##4", "aed##4", True),
        ("13#a#b5", "13#e#b5", True),
    ],
)
def test_two_strings_in_backspace_compare_func_are_equal(
    first_string: str, second_string: str, expected_result: bool
):

    assert backspace_compare(first_string, second_string)


@pytest.mark.parametrize(
    ["first_string", "second_string", "expected_result"],
    [
        ("", "a", False),
        ("a", "b", False),
        ("a#", "b", False),
        ("a#a", "b", False),
        ("a#a", "##", False),
        ("a#a", "b#", False),
        ("ab##7", "ab##8", False),
        ("1ab##7", "1ab##8", False),
        ("a#bc#", "a#dc#", False),
    ],
)
def test_two_strings_in_backspace_compare_func_are_not_equal(
    first_string: str, second_string: str, expected_result: bool
):

    assert backspace_compare(first_string, second_string) is False
