from typing import List


class Solution:
    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = float('inf')
        total = 0
        left = 0
        for right in range(n):
            total += nums[right]
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if result == float('inf') else result