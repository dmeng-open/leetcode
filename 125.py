# Time: O(n)
# Space: O(1)
class Solution:
    def isPalindrome(self, input: str) -> bool:
        n = len(input)
        i = 0
        j = n - 1
        while (i < j):
            while i < j and not input[i].isalnum():
                i += 1
            while i < j and not input[j].isalnum():
                j -= 1
            if input[i].lower() != input[j].lower():
                return False
            i += 1
            j -= 1
        return True