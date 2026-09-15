from typing import List

# O(n) | O(1)
def compress(chars: List[str]) -> int:
    read = end = write = 0
    while end < len(chars):
        while end < len(chars) and chars[read] == chars[end]:
            end += 1
        count = end - read
        chars[write] = chars[read]
        write += 1
        if count > 1:
            for c in str(count):
                chars[write] = c
                write += 1
        read = end
    return write
