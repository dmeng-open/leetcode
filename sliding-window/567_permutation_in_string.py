from collections import Counter


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)

        if k > n:
            return False

        need = Counter(s1)
        window = Counter()

        for right in range(n):
            window[s2[right]] += 1

            if right >= k:
                left = right - k
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    window.pop(s2[left])

            if right >= k - 1 and window == need:
                return True

        return False