from collections import Counter


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        n = len(s2)

        if window_len > n:
            return False

        need = Counter(s1)
        window = Counter()

        for right in range(n):
            window[s2[right]] += 1

            if right >= window_len:
                left = right - window_len
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    window.pop(s2[left])

            if right >= window_len - 1 and window == need:
                return True

        return False
