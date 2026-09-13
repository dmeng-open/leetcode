from typing import List


class Solution:
    def num_subarrays_with_sum(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        def lte(k: int) -> int:
            result = 0
            total = 0
            left = 0
            for right in range(n):
                total += nums[right]
                while total > k:
                    total -= nums[left]
                    left += 1
                result += right - left + 1
            return result

        return lte(goal) - lte(goal - 1)