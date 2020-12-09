import os

import pytest

from homework8.tasks.task1 import KeyValueStorage


@pytest.fixture(scope="module")
def path_to_dir():
    return (
        os.path.abspath(os.path.dirname(__file__))
        + "/The_directory_with_the_files_to_test"
    )


def test_correct_keys_and_values(path_to_dir):
    file_path = path_to_dir + "/file1.txt"
    ins = KeyValueStorage(file_path)

    assert ins["name"] == "kek"


def test_correct_keys_and_values2(path_to_dir):
    file_path = path_to_dir + "/file2.txt"
    ins = KeyValueStorage(file_path)

    assert ins["attr"] == "(9,)"


def test_invalid_attribute(path_to_dir):
    file_path = path_to_dir + "/file3.txt"

    with pytest.raises(ValueError) as message:
        KeyValueStorage(file_path)

    assert "the value 1 cannot be an attribute." in str(message.value)


def test_invalid_attribute_without_numbers(path_to_dir):
    file_path = path_to_dir + "/file4.txt"

    with pytest.raises(ValueError) as message:
        KeyValueStorage(file_path)

    assert "the value a_- cannot be an attribute." in str(message.value)


def test_built_in_attributes_remain(path_to_dir):
    file_path = path_to_dir + "/file5.txt"
    ins = KeyValueStorage(file_path)

    with pytest.raises(KeyError) as message:
        ins["__doc__"]

    assert "__doc__" in str(message.value)
