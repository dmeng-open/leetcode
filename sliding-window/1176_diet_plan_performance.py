from ast import List


class Solution:
    # O(n) | O(k)
    def diet_plan_performance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        def eval(total: int) -> int:
            if total < lower:
                return -1
            if total > upper:
                return 1
            return 0

        n = len(calories)
        total = sum(calories[:k]) # O(k) space
        result = eval(total)
        for right in range(k, n):
            delta = calories[right] - calories[right - k]
            total += delta
            result += eval(total)
        return result

    def diet_plan_performance_v2(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        total = result = 0
        for i in range(n):
            total += calories[i]
            if i >= k:
                total -= calories[i - k]
            if i >= k - 1:
                if total < lower:
                    result -= 1
                elif total > upper:
                    result += 1
        return result