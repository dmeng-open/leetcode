from typing import List

class Solution:
    def longest_ones(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        count = 0
        left = 0
        for right in range(n):
            count += nums[right] == 1
            while right - left + 1 - count > k:
                count -= nums[left] == 1
                left += 1
            result = max(result, right - left + 1)
        return result