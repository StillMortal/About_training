import os
from typing import List

import pytest

from homework2.tasks import task1


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (
            os.path.abspath(os.path.dirname(__file__)) + "/data.txt",
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Werkstättenlandschaft",
                "Selbstverständlich",
                "Schicksalsfiguren",
                "Werkstättenlandschaft",
                "Vorausgeschickt",
                "Außerordentliche",
                "Friedensabstimmung",
            ],
        ),
        (
            os.path.abspath(os.path.dirname(__file__)) + "/file_for_test_number_1.txt",
            [
                "defg",
                "abc",
                "abcdɶ",
                "abcde",
                "abc",
                "abc",
                "ɵab",
                "def",
                "abcdefg",
                "abcdefgh",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(path_to_file: str, expected_result: List[str]):
    actual_result = task1.get_longest_diverse_words(path_to_file)

    print(actual_result)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/data.txt", "›"),
        (
            os.path.abspath(os.path.dirname(__file__)) + "/file_for_test_number_1.txt",
            "ɶ",
        ),
    ],
)
def test_get_rarest_char(path_to_file: str, expected_result: str):
    actual_result = task1.get_rarest_char(path_to_file)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/data.txt", 5305),
        (
            os.path.abspath(os.path.dirname(__file__)) + "/file_for_test_number_1.txt",
            13,
        ),
    ],
)
def test_count_punctuation_chars(path_to_file: str, expected_result: int):
    actual_result = task1.count_punctuation_chars(path_to_file)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/data.txt", 2972),
        (os.path.abspath(os.path.dirname(__file__)) + "/file_for_test_number_1.txt", 3),
    ],
)
def test_count_non_ascii_chars(path_to_file: str, expected_result: int):
    actual_result = task1.count_non_ascii_chars(path_to_file)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/data.txt", "ä"),
        (
            os.path.abspath(os.path.dirname(__file__)) + "/file_for_test_number_1.txt",
            "ɵ",
        ),
    ],
)
def test_get_most_common_non_ascii_char(path_to_file: str, expected_result: str):
    actual_result = task1.get_most_common_non_ascii_char(path_to_file)

    assert actual_result == expected_result
