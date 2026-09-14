from collections import defaultdict
from typing import List


class Solution:
    def subarrays_with_k_distinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def lte(k: int):
            seen = defaultdict(int)
            result = 0
            left = 0
            for right in range(n):
                seen[nums[right]] += 1
                while len(seen) > k:
                    seen[nums[left]] -= 1
                    if seen[nums[left]] == 0:
                        seen.pop(nums[left])
                    left += 1
                result += right - left + 1
            return result
        return lte(k) - lte(k - 1)
