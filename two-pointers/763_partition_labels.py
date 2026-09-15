from typing import List

# O(n) | O(1) fixed size map
def partition_labels(s: str) -> List[int]:
    last = [0] * 26
    for idx, c in enumerate(s):
        last[ord(c) - ord('a')] = idx
    start = end = 0
    result = []
    for idx, c in enumerate(s):
        end = max(end, last[ord(c) - ord('a')])
        if idx == end:
            result.append(end - start + 1)
            start = idx + 1
    return result
