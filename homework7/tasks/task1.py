"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool

"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: Any, element: Any, num_of_occurrences: int = 0) -> int:
    """Finds the number of occurrences of an element in the tree.

    Args:
        tree: Where to search for the element.
        element: Element the number of occurrences to find.
        num_of_occurrences: The counter element

    Returns:
        Number of occurrences.

    """
    if element == tree:
        return num_of_occurrences + 1
    elif isinstance(tree, (list, tuple, set)):
        for node in tree:
            num_of_occurrences += find_occurrences(node, element)
    elif isinstance(tree, dict):
        for key in tree:
            num_of_occurrences += find_occurrences(key, element)
            num_of_occurrences += find_occurrences(tree[key], element)
    return num_of_occurrences


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
