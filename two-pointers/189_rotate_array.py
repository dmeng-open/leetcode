from typing import List

# 1 2 3 4 5 6 7 | 3
# 7 6 5 4 3 2 1
#       k
# 5 6 7 1 2 3 4   
def rotate(nums: List[int], k: int) -> None:
    def flip(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    n = len(nums)
    k %= n
    flip(0, n - 1)
    flip(0, k - 1)
    flip(k, n - 1)
