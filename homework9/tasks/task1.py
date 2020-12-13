"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]

"""
import heapq
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merges integers in non-decreasing order from sorted files.

    Args:
        file_list: A list containing file paths.

    Returns:
        Generator.

    """
    numbers = []
    heapq.heapify(numbers)

    for file_number, path in enumerate(file_list):
        with open(path) as data:
            heapq.heappush(numbers, [int(data.readline()), file_number, 0])

    while numbers:
        min_value, file_number, num_of_the_last_used_string = heapq.heappop(numbers)
        yield min_value

        next_num = ""
        with open(file_list[file_number]) as data:
            for line_num, line in enumerate(data):
                if line_num == num_of_the_last_used_string + 1:
                    next_num = line
                    break

        if next_num:
            heapq.heappush(numbers, [int(next_num), file_number, line_num])
