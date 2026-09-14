from typing import List


class Solution:
    def count_subarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        total = 0
        left = 0
        for right in range(n):
            total += nums[right]
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            result += right - left + 1
        return result