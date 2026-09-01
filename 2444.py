from typing import List


class Solution:
    def count_subarray_with_fixed_bounds(self, nums: List[int], low: int, high: int) -> int:
        last_low_index = last_high_index = last_out_of_bound_index = -1
        count = 0
        for i, num in enumerate(nums):
            if num < low or num > high:
                last_out_of_bound_index = i
            if num == low:
                last_low_index = i
            if num == high:
                last_high_index = i
            count += max(0, min(last_low_index, last_high_index) - last_out_of_bound_index)
        return count

    def count_subarray_with_fixed_bounds_v2(self, nums: List[int], low: int, high: int) -> int:
        last_low_index = last_high_index = last_out_of_bound_index = -1
        count = 0
        for i, num in enumerate(nums):
            if num < low or num > high:
                last_out_of_bound_index = i
                last_high_index = -1
                last_low_index = -1
            if num == low:
                last_low_index = i
            if num == high:
                last_high_index = i
            if last_low_index != -1 and last_high_index != -1:
                count += min(last_low_index, last_high_index) - last_out_of_bound_index
        return count