from typing import List
# T: O(n)
# S: O(1)
class Solution:
    def squares(self, ordered: List[int]) -> List[int]:
        n = len(ordered)
        result = [0] * n
        i, j, k = 0, n - 1, n - 1
        while i <= j:
            if abs(ordered[i]) > abs(ordered[j]):
                result[k] = ordered[i] * ordered[i]
                i += 1
            else:
                result[k] = ordered[j] * ordered[j]
                j -= 1
            k -= 1
        return result