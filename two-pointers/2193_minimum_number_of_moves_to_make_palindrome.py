# T: O(n)
# S: O(n)
# a b b a
#     left
#       right

# l e t t e l
#       left
#         right
def min_moves_to_make_palindrome(s: str) -> int:
    arr = list(s) # S: O(n)
    count = left = 0
    right = len(arr) - 1
    while left < right: # O(n)
        if arr[left] != arr[right]:
            match = right
            while match > left and arr[left] != arr[match]: # O(n)
                match -= 1
            if match == left:
                count += len(arr) // 2 - left
                left += 1
            else:
                while match < right:
                    arr[match], arr[match + 1] = arr[match + 1], arr[match]
                    match += 1
                    count += 1
                # Optional: The else block will be entered for the next iteration 
                # left += 1
                # right -= 1
        else:
            left += 1
            right -= 1
    return count
