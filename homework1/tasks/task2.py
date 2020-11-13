"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Whether the sequence is a Fibonacci sequence.

    Args:
        data: The original sequence to check.

    Returns:
        True if successful, False otherwise.

    """
    data = [int(i) for i in data]
    if len(data) < 3:
        return False
    elif data[0] != 0 or data[1] != 1:
        return False
    else:
        previous = 0
        current = 1
        for elem in data[2:]:
            previous, current = current, previous + current
            if elem != current:
                return False

    return True
