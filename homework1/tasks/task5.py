"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_sum(nums: List[int], k: int) -> int:
    """Finds a sub-array with length less equal to "k", with maximal sum.

    Args:
        nums: The initial list where we find the subarray with the max sum.
        k: Size of the subarray.

    Returns:
        Maximal sum.

    """
    maximal_sum = nums[0] if len(nums) > 0 else 0

    for num_of_elements in range(1, k + 1):
        num_of_used = 0
        local_sum = 0
        for ind, elem in enumerate(nums):
            if num_of_used < num_of_elements:
                num_of_used += 1
                local_sum += elem
                maximal_sum = max(maximal_sum, local_sum)
            else:
                local_sum += elem - nums[ind - num_of_used]
                maximal_sum = max(maximal_sum, local_sum)

    return maximal_sum
