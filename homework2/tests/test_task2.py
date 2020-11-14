
from typing import List, Tuple

import pytest

from homework2.tasks.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["list_of_numbers", "expected_result"],
    [
        ([1, 2, 3, 3, 2, 2], (2, 1)),
        ([1, 2, 3, 3], (3, 2)),
        ([2, 2, 3, 3], (2, 3)),
        ([5], (5, 5)),
    ],
)
def test_major_and_minot_elem(
    list_of_numbers: List[int], expected_result: Tuple[int, int]
):
    actual_result = major_and_minor_elem(list_of_numbers)

    assert actual_result == expected_result
