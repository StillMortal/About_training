"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]

"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Finds combinations.

    Args:
        *args: Contains lists.

    Returns:
        All possible lists of K items.
    """

    def generator_of_combinations(part_of_the_comb: List[Any]) -> List[Any]:
        """Generates combinations.

        Args:
            part_of_the_comb: Contains part ot the combination.

        Returns:
            One combination.

        """
        if len(part_of_the_comb) == k:
            yield part_of_the_comb
        else:
            for elem in args[len(part_of_the_comb)]:
                yield from generator_of_combinations(part_of_the_comb + [elem])

    k = len(args)

    list_of_combinations = []
    for comb in generator_of_combinations([]):
        list_of_combinations.append(comb)

    return list_of_combinations
