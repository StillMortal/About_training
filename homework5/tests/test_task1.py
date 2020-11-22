import datetime
from typing import Any, Tuple

import pytest

from homework5.tasks.task1 import Homework, Student, Teacher


@pytest.mark.parametrize(
    ["first_name", "last_name", "expected_result"],
    [
        ("Valya", "Petrova", ("Valya", "Petrova")),
        ("Valya", "", ("Valya", "")),
    ],
)
def test_check_first_and_last_names(
    first_name: str, last_name: str, expected_result: Tuple[str]
):
    actual_result = Student(last_name, first_name)
    actual_result2 = Teacher(last_name, first_name)

    assert (
        (actual_result.first_name, actual_result.last_name)
        == (actual_result2.first_name, actual_result2.last_name)
        == expected_result
    )


@pytest.mark.parametrize(
    ["text", "deadline", "expected_result"],
    [
        ("Do it", 7, ("Do it", datetime.timedelta(7))),
        ("Just do it", 0, ("Just do it", datetime.timedelta(0))),
    ],
)
def test_creation_of_a_homework_object(
    text: str, deadline: int, expected_result: Tuple[Any]
):
    actual_result = Teacher.create_homework(text, deadline)

    assert (actual_result.text, actual_result.deadline) == expected_result


def test_overdue_homework(capsys):
    actual_result = Teacher.create_homework("Do it", 0)
    actual_result2 = Student.do_homework(actual_result)
    captured = capsys.readouterr()

    assert (
        actual_result.is_active() is False
        and actual_result2 is None
        and captured.out == "You are late.\n"
    )


def test_there_is_still_time_for_homework():
    actual_result = Teacher.create_homework("Just do it", 1)
    actual_result2 = Student.do_homework(actual_result)

    assert actual_result.is_active() is True and isinstance(actual_result2, Homework)
