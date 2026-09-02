from typing import List

# O(n) | O(1) fixed size map
def partition(s: str) -> List[int]:
    last = [0] * 26
    for i, c in enumerate(s):
        last[ord(c) - ord('a')] = i
    start = end = 0
    result = []
    for i, c in enumerate(s):
        end = max(end, last[ord(c) - ord('a')])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result