from typing import List

# O(n) | O(k)
def find_max_average(self, nums: List[int], k: int) -> float:
    n = len(nums)
    total = sum(nums[:k])
    max_total = total
    for i in range(k, n):
        delta = nums[i] - nums[i - k]
        total += delta
        max_total = max(max_total, total)
    return max_total / k