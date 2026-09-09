from typing import List

# 1 2 3 4 5 6 7 | 3
# 7 6 5 4 3 2 1
#       k
# 5 6 7 1 2 3 4   
def rotate(nums: List[int], k: int) -> None:
    def flip(i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    n = len(nums)
    k %= n
    flip(0, n - 1)
    flip(0, k - 1)
    flip(k, n - 1)