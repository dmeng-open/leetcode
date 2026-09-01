from typing import List

# T: O(n)
# S: O(1)
class Solution:
    # 0 0 1 1 2 2
    #     r
    #     w
    #       b
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        r = w = 0
        b = n - 1
        # w <= b
        # 1 0
        # w
        #   b
        while w <= b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                r += 1
                w += 1
            elif nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            else:
                w += 1