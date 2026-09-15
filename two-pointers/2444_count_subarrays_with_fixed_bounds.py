from typing import List


def count_subarrays(nums: List[int], low: int, high: int) -> int:
    last_low_index = last_high_index = last_out_of_bound_index = -1
    count = 0
    for idx, num in enumerate(nums):
        if num < low or num > high:
            last_out_of_bound_index = idx
        if num == low:
            last_low_index = idx
        if num == high:
            last_high_index = idx
        count += max(0, min(last_low_index, last_high_index) - last_out_of_bound_index)
    return count

def count_subarrays_v2(nums: List[int], low: int, high: int) -> int:
    last_low_index = last_high_index = last_out_of_bound_index = -1
    count = 0
    for idx, num in enumerate(nums):
        if num < low or num > high:
            last_out_of_bound_index = idx
            last_high_index = -1
            last_low_index = -1
        if num == low:
            last_low_index = idx
        if num == high:
            last_high_index = idx
        if last_low_index != -1 and last_high_index != -1:
            count += min(last_low_index, last_high_index) - last_out_of_bound_index
    return count
