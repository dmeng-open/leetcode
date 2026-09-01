# T: O(n)
# S: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split() # S: O(n)
        i, j = 0, len(arr) - 1
        while i < j: # O(n)
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return " ".join(arr)