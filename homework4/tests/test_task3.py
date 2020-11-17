import sys
from homework4.tasks.task3 import my_precious_logger


def test_my_out(capsys):
    my_precious_logger("not an error")
    captured = capsys.readouterr()

    assert captured.out == "not an error"


def test_my_err(capsys):
    my_precious_logger("error")
    captured = capsys.readouterr()

    assert captured.err == "error"
