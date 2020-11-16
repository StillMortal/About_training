import pytest
from homework3.tasks.task4 import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"], [(153, True), (9, True), (10, False), (11, False)]
)
def test_is_armstrong(number: int, expected_result: bool):
    actual_result = is_armstrong(number)

    assert actual_result == expected_result
