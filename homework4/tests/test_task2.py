from unittest.mock import Mock, patch

import pytest

from homework4.tasks.task2 import count_dots_on_i


def test_bad():
    with pytest.raises(ValueError):
        count_dots_on_i_negative()


@patch("homework4.tasks.task2.requests.get")
def count_dots_on_i_negative(mock_get):
    mock_get.return_value = ValueError

    count_dots_on_i("broken_url")


@patch("homework4.tasks.task2.requests.get")
def test_count_dots_on_i_positive(mock_get):
    count_dots_on_i = Mock()
    count_dots_on_i.return_value = 59

    mock_get.return_value.ok = True

    assert count_dots_on_i("https://example.com/")
