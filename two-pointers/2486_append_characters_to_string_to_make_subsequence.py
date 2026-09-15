# coaching
# s_idx
# coding
#   t_idx
def append_characters(s: str, t: str) -> None:
    s_idx = t_idx = 0
    while s_idx < len(s) and t_idx < len(t):
        if s[s_idx] == t[t_idx]:
            t_idx += 1
        s_idx += 1
    return len(t) - t_idx
