def merge_alternately(a: str, b: str) -> str:
    n, m = len(a), len(b)
    result = []
    a_idx = b_idx = 0
    while a_idx < n or b_idx < m:
        if a_idx < n:
            result.append(a[a_idx])
            a_idx += 1
        if b_idx < m:
            result.append(b[b_idx])
            b_idx += 1
    return ''.join(result)
