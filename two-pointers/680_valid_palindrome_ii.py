# T: O(n)
# S: O(1)
# a b c a
#  left
#     right

# a b x c a
#   left
#        right

# a b c c a
#   left
#     right
def valid_palindrome(s: str) -> bool:
    def check(left, right) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    n = len(s)
    left = 0
    right = n - 1
    while left < right:
        if (s[left] == s[right]):
            left += 1
            right -= 1
        else:
            return check(left + 1, right) or check(left, right - 1)
    return True
            
    
