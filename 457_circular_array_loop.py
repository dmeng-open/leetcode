# Circular array
# Non-zero integers
# Cycle nodes either all forward or all backward
# No self-cycle
from typing import List

# O(n) | O(1)
class Solution:
    def circular_array_loop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next(i: int) -> int:
            return (i + nums[i]) % n

        def advance(i: int, forward: bool) -> int:
            if (nums[i] == 0 or (nums[i] > 0) != forward):
                return -1
            j = next(i)
            if i == j:
                return -1
            return j

        for i in range(n):
            j = k = i
            forward = nums[i] > 0
            while True:
                j = advance(j, forward)
                if j == -1:
                    break
                k = advance(k, forward)
                if k == -1:
                    break
                k = advance(k, forward)
                if k == -1:
                    break
                if j == k:
                    return True
            x = i
            while nums[x] != 0 and (nums[x] > 0) == forward:
                y = next(x)
                nums[x] = 0
                x = y
        return False
