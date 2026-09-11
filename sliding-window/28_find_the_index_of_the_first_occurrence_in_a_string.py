class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        for right in range(m - 1, n):
            left = right - m + 1
            if haystack[left:right + 1] == needle: # O(m) | O(m)
                return left

        return -1