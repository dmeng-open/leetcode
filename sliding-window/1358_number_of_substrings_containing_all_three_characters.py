class Solution:
    def number_of_substrings(self, s: str) -> int:
        n = len(s)

        counter = {
            'a': 0,
            'b': 0,
            'c': 0
        }

        def valid() -> bool:
            return (
                counter['a'] > 0 and
                counter['b'] > 0 and 
                counter['c'] > 0)

        result = 0
        left = 0
        for right in range(n):
            counter[s[right]] += 1
            while valid():
                counter[s[left]] -= 1
                left += 1
            result += left

        return result