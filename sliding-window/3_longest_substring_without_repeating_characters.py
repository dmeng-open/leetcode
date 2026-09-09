# O(n) | O(1)
def length_of_longest_substring(s: str) -> int:
    n = len(s)
    seen = set()
    i = result = 0
    for j in range(n):
        while s[j] in seen:
            seen.remove(s[i])
            i += 1
        seen.add(s[j])
        result = max(result, j - i + 1)
    return result