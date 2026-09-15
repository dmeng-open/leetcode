from typing import List

# O(n) | O(1)
def circular_array_loop(nums: List[int]) -> bool:
    n = len(nums)

    def next(idx: int) -> int:
        return (idx + nums[idx]) % n

    def advance(idx: int, forward: bool) -> int:
        nxt = next(idx)
        # 1. Self loop
        # 2. nums[idx] = 0
        if idx == nxt:
            return -1
        # 1. nums[nxt] = 0
        # 2. nums[nxt] opposite direction
        if nums[nxt] == 0 or (nums[nxt] > 0) != forward:
            return -1
        return nxt

    for start in range(n):
        if nums[start] == 0:
            continue
        slow = fast = start
        forward = nums[start] > 0
        while True:
            slow = advance(slow, forward)
            if slow == -1:
                break
            fast = advance(fast, forward)
            if fast == -1:
                break
            fast = advance(fast, forward)
            if fast == -1:
                break
            if slow == fast:
                return True
        # Mark invalid path to prevent recompute
        idx = start
        while nums[idx] != 0 and (nums[idx] > 0) == forward:
            nxt = next(idx)
            nums[idx] = 0
            idx = nxt

    return False
