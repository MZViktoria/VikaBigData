from typing import List
import pytest
nums = [5, 2, -3, -3, 6, 8, 3, 8, -7, -9, 1, 9, -5, 7, -5, 3, 2]
k = 5


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    z = 0
    sum_max = 0
    while z < k:
        sum_max += nums[z]
        z += 1
    z = 1
    while z <= len(nums) - k:
        try:
            t=z
            sum_temp = 0
            while t < z+k:
                sum_temp += nums[t]
                t += 1
            if sum_temp > sum_max:
                sum_max = sum_temp
            z += 1
        except IndexError:
            break

    return print(sum_max)


find_maximal_subarray_sum(nums, k)
