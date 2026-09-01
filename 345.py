class Solution:
    def reverse(self, s: str) -> None:
        vowels = set("aeiouAEIOU")
        result = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and result[i] not in vowels:
                i += 1
            while i < j and result[j] not in vowels:
                j -= 1
            result[i], result[j] = result[j], result[i]
            i += 1
            j -= 1
        return ''.join(result)