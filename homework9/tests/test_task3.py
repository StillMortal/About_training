import os
from pathlib import Path

import pytest

from homework9.tasks.task3 import universal_file_counter


@pytest.fixture(scope="module")
def directory_path():
    return Path(os.path.abspath(os.path.dirname(__file__)))


def test_there_are_files_with_the_extension_but_there_is_no_tokenizer(directory_path):
    result = universal_file_counter(directory_path, "txt")

    assert result == 6


def test_there_are_files_with_the_extension_but_there_is_no_tokenizer2(directory_path):
    result = universal_file_counter(directory_path, "py")

    assert result == 127


def test_there_are_files_with_the_extension_but_there_is_a_tokenizer(directory_path):
    result = universal_file_counter(directory_path, "txt", str.split)

    assert result == 6


def test_there_are_files_with_the_extension_but_there_is_a_tokenizer2(directory_path):
    result = universal_file_counter(directory_path, "py", str.split)

    assert result == 244
