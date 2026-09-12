from ast import List


class Solution:
    def repeated_dna_sequences(self, s: str) -> List[str]:
        n = len(s)
        seen = set()
        result = set()
        for right in range(9, n):
            sequence = s[right - 9:right + 1]
            if sequence in seen:
                result.add(sequence)
            else:
                seen.add(sequence)
        return list(result)