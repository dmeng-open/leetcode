class Solution:
    def merge(a: str, b: str) -> str:
        n, m = len(a), len(b)
        result = []
        i = j = 0
        while i < n or j < m:
            if i < n:
                result.append(a[i])
                i += 1
            if j < m:
                result.append(b[j])
                j += 1
        return ''.join(result)