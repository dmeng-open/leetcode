class Solution:
    def min_window(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        best_len = float('inf')
        best_left = 0
        k = 0
        right = 0
        while right < n:
            if s1[right] == s2[k]:
                k += 1
            if k == m:
                k = m - 1
                left = right
                while k >= 0:
                    if s1[left] == s2[k]:
                        k -= 1
                    left -= 1
                left += 1
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                right = left
                k = 0
            right += 1
        return '' if best_len == float('inf') else s1[best_left:best_left + best_len] 