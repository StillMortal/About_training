"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that
A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Number of tuples (i, j, k, l) such that a[i] + b[j] + c[k] + d[l] is zero.

    Args:
        a: The first list.
        b: The second list.
        c: The third list.
        d: The fourth list.

    Returns:
        Number of tuples.

    """
    element_sum_of_a_and_b = [a_i + b_i for a_i in a for b_i in b]
    element_sum_of_c_and_d = [c_i + d_i for c_i in c for d_i in d]

    return [
        i + j for i in element_sum_of_a_and_b for j in element_sum_of_c_and_d
    ].count(0)
