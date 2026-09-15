from typing import List
# T: O(n)
# S: O(1)
def sorted_squares(ordered: List[int]) -> List[int]:
    n = len(ordered)
    result = [0] * n
    left, right, write = 0, n - 1, n - 1
    while left <= right:
        if abs(ordered[left]) > abs(ordered[right]):
            result[write] = ordered[left] ** 2
            left += 1
        else:
            result[write] = ordered[right] ** 2
            right -= 1
        write -= 1
    return result
