from typing import List

# O(n) | O(n)
def find_repeated_dna_sequences(s: str) -> List[str]:
    n = len(s)
    seen = set()
    result = set()
    for i in range(n - 9):
        sub = s[i: i + 10]
        if sub in seen:
            result.add(sub)
        seen.add(sub)
    return list(result)