# coaching
# i
# coding
#   j
def append_characters(s: str, t: str) -> None:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return len(t) - j
