# O(m x n) | O(1) or O(n)
def str_str(haystack: str, needle: str) -> int:
    m = len(haystack)
    n = len(needle)
    # 8 - 6 = 2 -> 2 + 1 = 3
    for i in range(m - n + 1):
        # i = 0 | 0 + 6 = 6
        if haystack[i:i + n] == needle:
            return i
        # j = 0
        # while j < n and haystack[i + j] == needle[j]:
        #     j += 1
        # if j == n:
        #     return i
    return -1