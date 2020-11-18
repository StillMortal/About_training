import os

import pytest

from homework4.tasks.task1 import read_magic_number


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [
        (
            os.path.abspath(os.path.dirname(__file__))
            + "/dir_for_test_number_1/file.txt",
            True,
        ),
        (
            os.path.abspath(os.path.dirname(__file__))
            + "/dir_for_test_number_1/file2.txt",
            True,
        ),
    ],
)
def test_read_magic_number_positive(path: str, expected_result: bool):
    actual_result = read_magic_number(path)

    assert actual_result is expected_result


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [
        (
            os.path.abspath(os.path.dirname(__file__))
            + "/dir_for_test_number_1/file3.txt",
            False,
        ),
        (
            os.path.abspath(os.path.dirname(__file__))
            + "/dir_for_test_number_1/file4.txt",
            False,
        ),
    ],
)
def test_read_magic_number_negative(path: str, expected_result: bool):
    actual_result = read_magic_number(path)

    assert actual_result is expected_result


@pytest.mark.parametrize(
    ["path"],
    [
        (
            os.path.abspath(os.path.dirname(__file__))
            + "/dir_for_test_number_1/file5.txt",
        ),
        (
            os.path.abspath(os.path.dirname(__file__))
            + "/dir_for_test_number_1/file6.txt",
        ),
        (
            os.path.abspath(os.path.dirname(__file__))
            + "/dir_for_test_number_1/file7.txt",
        ),
    ],
)
def test_read_magic_number_exception(path: str):
    with pytest.raises(ValueError):
        read_magic_number(path)
