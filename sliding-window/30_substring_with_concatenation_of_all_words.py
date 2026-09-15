from collections import Counter, defaultdict
from typing import List


class Solution:
    def find_substring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        word_len = len(words[0])
        need = Counter(words)
        result = []
        for offset in range(word_len):
            seen = defaultdict(int)
            left = right = offset
            count = 0
            while right + word_len <= n:
                current = s[right:right + word_len]
                right += word_len
                if current not in need:
                    seen.clear()
                    count = 0
                    left = right
                    continue
                seen[current] += 1
                count += 1
                while seen[current] > need[current]:
                    seen[s[left:left + word_len]] -= 1
                    left += word_len
                    count -= 1
                if count == m:
                    result.append(left)
        return result
