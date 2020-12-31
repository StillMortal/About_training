from collections import Sequence

import pytest

from homework1.tasks.task2 import check_fibonacci


@pytest.mark.parametrize(
    ["seq", "expected_result"],
    [
        ([], False),
        ((0,), False),
        ([0, 1, 1, 2, 3, 5], True),
        ((1,), False),
        ([1, 1, 2], False),
        ((1, 1, 2, 3, 4), False),
    ],
)
def test_fibonacci(seq: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(seq)

    assert actual_result == expected_result
