from typing import List

# O(n) | O(1)
class Solution:
    def dup(self, nums: List[int]) -> int:
        x = y = 0
        while x != y:
            x = nums[x]
            y = nums[nums[y]]
            if x == y:
                break
        x = 0
        while x != y:
            x = nums[x]
            y = nums[y]
        return nums[x]