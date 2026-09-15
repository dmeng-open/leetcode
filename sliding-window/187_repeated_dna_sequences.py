from typing import List


class Solution:
    def find_repeated_dna_sequences(self, s: str) -> List[str]:
        window_len = 10
        n = len(s)
        result = set()
        seen = set()
        for left in range(n - window_len + 1):
            sequence = s[left:left + window_len]
            if s[left:left + window_len] in seen:
                result.add(sequence)
            else:
                seen.add(sequence)
        return list(result)
