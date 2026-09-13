from collections import Counter


class Solution:
    def min_window(self, s: str, t: str) -> str:
        n = len(s)
        required = Counter(t)
        window = Counter()
        required_count = len(required)
        formed = 0
        left = 0
        best_len = float('inf')
        best_left = 0
        for right in range(n):
            window[s[right]] += 1
            if window[s[right]] == required[s[right]]:
                formed += 1
            while formed == required_count:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                window[s[left]] -= 1
                if window[s[left]] < required[s[left]]:
                    formed -= 1
                left += 1
        return '' if best_len == float('inf') else s[best_left:best_left + best_len]