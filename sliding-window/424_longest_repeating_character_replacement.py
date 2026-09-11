# A A B A B B B B B A | k = 1
#     L
#               R
# R - L + 1 = 5 | 5 - 4 = 1 <= 1
# max freq = 4
# size = 5
# freq map is for current window. 
# Therefore, whenever the max freq gets updated, all the most freq chars are in the current window
class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        result = 0
        freq = {}
        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while right - left + 1 - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result