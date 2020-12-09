import os

import pytest

from homework8.tasks.task2 import TableData


@pytest.fixture(scope="function")
def names():
    ins = TableData(
        os.path.abspath(os.path.dirname(__file__)) + "/example.sqlite", "Presidents"
    )

    return ins


def test_the_correct_num_of_rows_in_the_database(names):

    assert len(names) == 3


def test_the_reference_to_the_row_by_name(names):

    assert names["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_checks_whether_the_name_is_in_the_database_positive(names):

    assert "Yeltsin" in names


def test_checks_whether_the_name_is_in_the_database_negative(names):

    assert "Obama" not in names


def test_iterator_protocol(names):

    for name in names:
        assert name in (
            ("Yeltsin", 999, "Russia"),
            ("Trump", 1337, "US"),
            ("Big Man Tyrone", 101, "Kekistan"),
        )
