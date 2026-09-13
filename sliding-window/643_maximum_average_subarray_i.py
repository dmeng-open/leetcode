from typing import List


class Solution:
    def find_max_average(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = sum(nums[:k])
        result = total
        for right in range(k, n):
            total += nums[right] - nums[right - k]
            result = max(result, total)
        return result / k