from typing import List

import pytest

from homework1.tasks.task4 import check_sum_of_four


@pytest.mark.parametrize(
    ["lists", "expected_result"],
    [
        (([1, 2, 3], [-7, -3, -1], [0, 0, 0], [1, 4, 5]), 9),
    ],
)
def test_sum_of_four(
    lists: (List[int], List[int], List[int], List[int]), expected_result: int
):
    actual_result = check_sum_of_four(*lists)

    assert actual_result == expected_result
