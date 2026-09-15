from typing import List


def remove_element(arr: List[int], k: int) -> int:
    write = 0
    for read in range(len(arr)):
        if arr[read] != k:
            arr[write] = arr[read]
            write += 1
    return write
