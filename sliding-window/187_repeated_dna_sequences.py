from typing import List


class Solution:
    def find_repeated_dna_sequences(self, s: str) -> List[str]:
        k = 10
        n = len(s)
        result = set()
        seen = set()
        for left in range(n - k + 1):
            sequence = s[left:left + k]
            if s[left:left + k] in seen:
                result.add(sequence)
            else:
                seen.add(sequence)
        return list(result)
