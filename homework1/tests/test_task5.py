from typing import List

import pytest
from homework1.tasks.task5 import find_maximal_sum


@pytest.mark.parametrize(
    ["list_and_length", "expected_result"],
    [
        (([], 1), 0),
        (([1, 2, 3, 99, -1, 102, 4, 5, 6], 3), 200),
        (([-3, -2, -1], 2), -1),
        (([-1, 97, -3], 3), 97),
    ],
)
def test_maximal_sum(list_and_length: (List[int], int), expected_result: int):
    actual_result = find_maximal_sum(*list_and_length)

    assert actual_result == expected_result
