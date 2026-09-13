from typing import List


class Solution:
    def diet_plan_performance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        def score(total: int) -> int:
            if total < lower:
                return -1
            if total > upper:
                return 1
            return 0

        n = len(calories)
        total = sum(calories[:k])
        result = score(total)
        for right in range(k, n):
            total += calories[right] - calories[right - k]
            result += score(total)
        return result