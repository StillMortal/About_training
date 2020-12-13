import os
from pathlib import Path

from homework9.tasks.task3 import universal_file_counter


def test_there_are_files_with_the_extension_but_there_is_no_tokenizer():
    directory_path = Path(os.path.abspath(os.path.dirname(__file__)))
    result = universal_file_counter(directory_path, "txt")

    assert result == 10


def test_there_are_files_with_the_extension_but_there_is_no_tokenizer2():
    directory_path = Path(os.path.abspath(os.path.dirname(__file__) + "../.."))
    result = universal_file_counter(directory_path, "py")

    assert result == 241


def test_there_are_files_with_the_extension_but_there_is_a_tokenizer():
    directory_path = Path(os.path.abspath(os.path.dirname(__file__)))
    result = universal_file_counter(directory_path, "txt", str.split)

    assert result == 10


def test_there_are_files_with_the_extension_but_there_is_a_tokenizer2():
    directory_path = Path(os.path.abspath(os.path.dirname(__file__)))
    result = universal_file_counter(directory_path, "py", str.split)

    assert result == 199
