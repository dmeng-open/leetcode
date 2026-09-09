from typing import List

# O(n) | O(1)
def find_duplicate(nums: List[int]) -> int:
    x = y = 0
    while True:
        x = nums[x]
        y = nums[nums[y]]
        if x == y:
            break
    x = 0
    while x != y:
        x = nums[x]
        y = nums[y]
    return x
