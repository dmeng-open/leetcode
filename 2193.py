# T: O(n)
# S: O(n)
class Solution:
    # a b b a
    #     i
    #       j

    # l e t t e l
    #       i
    #         j
    def min_moves_to_make_palindrome(self, s: str) -> int:
        arr = list(s) # S: O(n)
        count = i = 0
        j = len(arr) - 1
        while i < j: # O(n)
            if arr[i] != arr[j]:
                k = j
                while k > i and arr[i] != arr[k]: # O(n)
                    k -= 1
                if k == i:
                    count += len(arr) // 2 - i
                    i += 1
                else:
                    while k < j:
                        arr[k], arr[k + 1] = arr[k + 1], arr[k]
                        k += 1
                        count += 1
            else:
                i += 1
                j -= 1
        return count
