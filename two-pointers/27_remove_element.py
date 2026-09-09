from typing import List


def remove_element(arr: List[int], k: int) -> int:
    i = 0
    for j in range(len(arr)):
        if arr[j] != k:
            arr[i] = arr[j]
            i += 1
    return i
