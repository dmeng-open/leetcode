# Time: O(n)
# Space: O(1)
def is_palindrome(input: str) -> bool:
    n = len(input)
    left = 0
    right = n - 1
    while (left < right):
        while left < right and not input[left].isalnum():
            left += 1
        while left < right and not input[right].isalnum():
            right -= 1
        if input[left].lower() != input[right].lower():
            return False
        left += 1
        right -= 1
    return True
