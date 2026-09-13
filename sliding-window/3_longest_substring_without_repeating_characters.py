class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        n = len(s)
        result = 0
        seen = set()
        left = 0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            result = max(result, right - left + 1)
        return result