from typing import List


class Solution:
    def longest(self, nums: List[int]) -> int:
        result = i = count = 0
        for j, num in enumerate(nums):
            count += num == 0
            while count > 1:
                count -= nums[i] == 0
                i += 1
            result = max(result, j - i)
        return result