from typing import Any, List

import pytest

from homework2.tasks.task3 import combinations


@pytest.mark.parametrize(
    ["lists", "expected_result"],
    [
        (([1], [3], [5]), [[1, 3, 5]]),
        (([1], [3, 4], [5]), [[1, 3, 5], [1, 4, 5]]),
        (([1, 2], [3, 4], [5]), [[1, 3, 5], [1, 4, 5], [2, 3, 5], [2, 4, 5]]),
        ((["p", "m", "b"], ["a"]), [["p", "a"], ["m", "a"], ["b", "a"]]),
    ],
)
def test_lists_of_K_items(lists: List[Any], expected_result: List[List]):
    actual_result = combinations(*lists)

    assert actual_result == expected_result
