from typing import List

# O(n) | O(1)
class Solution:
    def circular(self, nums: List[int]) -> bool:
        n = len(nums)

        def next(i: int) -> int:
            return (i + nums[i]) % n

        def advance(i: int, forward: bool) -> int:
            j = next(i)
            # 1. Self loop
            # 2. nums[i] = 0
            if i == j:
                return -1
            # 1. nums[j] = 0
            # 2. nums[j] opposite direction
            if nums[j] == 0 or (nums[j] > 0) != forward:
                return -1
            return j

        for i in range(n):
            x = y = i
            forward = nums[i] > 0
            while True:
                x = advance(x, forward)
                if x == -1:
                    break
                y = advance(y, forward)
                if y == -1:
                    break
                y = advance(y, forward)
                if y == -1:
                    break
                if x == y:
                    return True
            # Mark invalid path to prevent recompute
            x = i
            while nums[x] != 0 and (nums[x] > 0) == forward:
                j = next(x)
                nums[x] = 0
                x = j

        return False