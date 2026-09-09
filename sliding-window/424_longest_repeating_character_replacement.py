# O(n) | O(n)
def character_replacement(s: str, k: int) -> int:
    n = len(s)
    freq = {}
    result = max_freq = i = 0 
    for j in range(n):
        freq[s[j]] = freq.get(s[j], 0) + 1
        max_freq = max(max_freq, freq[s[j]])
        while j - i + 1 - max_freq > k:
            freq[s[i]] -= 1
            i += 1
        result = max(result, j - i + 1)
    return result