class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        n = len(s)
        left = 0
        result = 0
        seen = set()
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            result = max(result, right - left + 1)
        return result