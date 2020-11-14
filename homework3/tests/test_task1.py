from typing import Any, Callable, List, Tuple

import pytest
from homework3.tasks.task1 import cache


def func_for_the_test(a, b, c):
    return a + b + c


def args_len_plus_kwargs_len(*args, **kwargs):
    return len(args) + len(kwargs)


@pytest.mark.parametrize(
    ["func_to_check", "values", "expected_result"],
    [
        ((func_for_the_test, 1), ([1, 3, 5], [-1, 1, 3]), 9),
        ((func_for_the_test, 1), ([-1, 1, 3], [1, 3, 5]), 3),
    ],
)
def test_cache_func(func_to_check: Callable, values: Tuple[List], expected_result: Any):
    cache_func = cache(*func_to_check)
    actual_result = cache_func(*values[0])
    actual_result2 = cache_func(*values[1])

    assert actual_result == actual_result2 == expected_result


@pytest.mark.parametrize(
    ["func_to_check", "values", "expected_result"],
    [
        ((func_for_the_test, 1), ([1, 3, 5], [-1, 1, 3], [0, 0, 0]), 9),
        ((func_for_the_test, 1), ([-1, 1, 3], [1, 3, 5], [0, 0, 0]), 3),
    ],
)
def test_cache_func_negative(
    func_to_check: Callable, values: Tuple[List], expected_result: Any
):
    cache_func = cache(*func_to_check)
    actual_result = cache_func(*values[0])
    actual_result2 = cache_func(*values[1])
    actual_result3 = cache_func(*values[2])

    assert not actual_result == actual_result2 == actual_result3 == expected_result


@pytest.mark.parametrize(
    ["func_to_check", "values", "expected_result"],
    [
        ((args_len_plus_kwargs_len, 1), ([7], {"a": 5, "b": "c", "d": "e"}), 4),
        ((args_len_plus_kwargs_len, 1), ([1], {"e": 3}), 2),
    ],
)
def test_cache_func_with_kwargs(
    func_to_check: Callable, values: Tuple[List], expected_result: Any
):
    cache_func = cache(*func_to_check)
    actual_result = cache_func(*values[0])
    actual_result2 = cache_func(**values[1])

    assert not actual_result == actual_result2 == expected_result
