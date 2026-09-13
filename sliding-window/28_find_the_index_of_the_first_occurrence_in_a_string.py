class Solution:
        def str_str(self, haystack: str, needle: str) -> int:
            m = len(haystack)
            n = len(needle)

            for left in range(m - n + 1):
                if haystack[left:left + n] == needle:
                    return left

            return -1