from unittest.mock import patch

import pytest

from homework4.tasks.task2 import count_dots_on_i


@patch("homework4.tasks.task2.requests.get")
def test_count_dots_on_i_exception(mock_get):
    mock_get.return_value = Exception
    with pytest.raises(Exception) as info:
        count_dots_on_i("broken_url")

    assert "Unreachable broken_url" in str(info.value)


@patch("homework4.tasks.task2.count_dots_on_i")
@patch("homework4.tasks.task2.requests.get")
def test_count_dots_on_i(mock_requests_get, mock_count_dots_on_i):
    mock_requests_get.return_value.ok = True
    mock_requests_get.return_value.text = "Eleven minus nine"
    mock_count_dots_on_i.return_value = 2

    assert count_dots_on_i("https://example.com/") == 2
