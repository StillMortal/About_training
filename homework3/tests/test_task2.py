import os
from multiprocessing import Pool

import pytest
from homework3.tasks.task2 import slow_calculate


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (7, 15116),
        (15, 32153),
        (501, 1025932),
    ],
)
def test_slow_calculate(value: int, expected_result: int):
    with Pool() as p:
        actual_result = sum(
            p.map(
                slow_calculate,
                [i for i in range(value)],
                chunksize=value // os.cpu_count(),
            )
        )

    assert actual_result == expected_result
