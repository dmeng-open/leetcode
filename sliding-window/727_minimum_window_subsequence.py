class Solution:
    def min_window(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        best_len = float('inf')
        best_left = 0
        match = 0
        right = 0
        while right < n:
            if s1[right] == s2[match]:
                match += 1
            if match == m:
                match = m - 1
                left = right
                while match >= 0:
                    if s1[left] == s2[match]:
                        match -= 1
                    left -= 1
                left += 1
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                right = left
                match = 0
            right += 1
        return '' if best_len == float('inf') else s1[best_left:best_left + best_len] 
