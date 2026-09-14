from collections import defaultdict

class Solution:
    def number_of_substrings(self, s: str, k: int) -> int:
        n = len(s)
        counter = defaultdict(int)
        result = 0
        left = 0
        for right in range(n):
            counter[s[right]] += 1
            while counter[s[right]] >= k:
                counter[s[right]] -= 1
                left += 1
            result += left
        return result