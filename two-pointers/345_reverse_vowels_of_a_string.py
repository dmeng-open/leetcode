def reverse_vowels(s: str) -> None:
    vowels = set("aeiouAEIOU")
    result = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and result[left] not in vowels:
            left += 1
        while left < right and result[right] not in vowels:
            right -= 1
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return ''.join(result)
