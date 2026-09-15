from typing import List


def longest_subarray(nums: List[int]) -> int:
    result = left = count = 0
    for right, num in enumerate(nums):
        count += num == 0
        while count > 1:
            count -= nums[left] == 0
            left += 1
        result = max(result, right - left)
    return result
