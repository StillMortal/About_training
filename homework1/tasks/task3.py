"""
Write down the function, which reads input line-by-line,
and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_path: str) -> Tuple[int, int]:
    """Finds the maximum and minimum values in the file.

    Args:
        file_path: Path to file.

    Returns:
        A tuple containing the maximum and minimum values.

    """
    with open(file_path + ".txt") as fi:

        max_value = float("-inf")
        min_value = float("inf")

        for line in fi:
            values = [int(i) for i in line.split()]

            max_value = max(max_value, *values)

            min_value = min(min_value, *values)

    return max_value, min_value
