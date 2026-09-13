from collections import defaultdict
from typing import List


class Solution:
    def total_fruits(self, fruits: List[int]) -> int:
        n = len(fruits)
        seen = defaultdict(int)
        result = 0
        left = 0
        for right in range(n):
            seen[fruits[right]] += 1
            while len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    seen.pop(fruits[left])
                left += 1
            result = max(result, right - left + 1)
        return result