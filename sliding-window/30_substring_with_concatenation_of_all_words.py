from collections import Counter, defaultdict
from typing import List


class Solution:
    def find_substring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        k = len(words[0])
        need = Counter(words)
        result = []
        for offset in range(k):
            seen = defaultdict(int)
            left = right = offset
            count = 0
            while right + k <= n:
                current = s[right:right + k]
                right += k
                if current not in need:
                    seen.clear()
                    count = 0
                    left = right
                    continue
                seen[current] += 1
                count += 1
                while seen[current] > need[current]:
                    seen[s[left:left + k]] -= 1
                    left += k
                    count -= 1
                if count == m:
                    result.append(left)
        return result