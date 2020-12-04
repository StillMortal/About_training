from typing import Any

import pytest

from homework7.tasks.task1 import find_occurrences


@pytest.mark.parametrize(
    ["tree", "element", "expected_value"],
    [([], 3, 0), ("", (1,), 0), ({}, {1}, 0), (True, False, 0)],
)
def test_func_returns_zero_when_there_are_no_occurrences(
    tree: Any, element: Any, expected_value: int
):

    assert find_occurrences(tree, element) == expected_value


@pytest.mark.parametrize(
    ["tree", "element", "expected_value"],
    [
        ([[3, 4], 3, {1}], 3, 2),
        (("word", {"word": 7}, "abc"), "word", 2),
        (
            (
                ([1, 2], [[1, 2]]),
                {1: 2},
                {1, 2},
            ),
            [1, 2],
            2,
        ),
        ({True: 1, 1: True, 2: True}, True, 3),
    ],
)
def test_when_there_are_occurrences_of_an_element(
    tree: Any, element: Any, expected_value: int
):

    assert find_occurrences(tree, element) == expected_value
