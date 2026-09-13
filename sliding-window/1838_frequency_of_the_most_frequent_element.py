from typing import List


class Solution:
    def max_frequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        total = 0
        left = 0
        for right in range(n):
            total += nums[right]
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            result = max(result, right - left + 1)
        return result