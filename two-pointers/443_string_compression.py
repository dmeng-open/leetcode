from typing import List

# O(n) | O(1)
def compress(chars: List[str]) -> int:
    i = j = k = 0
    while j < len(chars):
        while j < len(chars) and chars[i] == chars[j]:
            j += 1
        count = j - i
        chars[k] = chars[i]
        k += 1
        if count > 1:
            for c in str(count):
                chars[k] = c
                k += 1
        i = j
    return k