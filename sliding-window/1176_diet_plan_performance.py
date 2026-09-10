from typing import List

# O(n) | O(1)
def diet_plan_performance(calories: List[int], k: int, lower: int, upper: int) -> int:
    n = len(calories)
    total = result = 0
    for i in range(n):
        total += calories[i]
        # i = 10 -> 0 [1, 10]
        if i >= k:
            total -= calories[i - k]
        # 1. i = 9 -> [0, 9] -> 10
        # 2. i = 10 -> [1, 10] -> 10
        if i >= k - 1:
            if total < lower:
                result -= 1
            elif total > upper:
                result += 1
    return result