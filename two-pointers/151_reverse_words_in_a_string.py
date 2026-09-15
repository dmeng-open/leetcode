# T: O(n)
# S: O(n)
def reverse_words(s: str) -> str:
    arr = s.split() # S: O(n)
    left, right = 0, len(arr) - 1
    while left < right: # O(n)
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return " ".join(arr)
