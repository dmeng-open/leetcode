from collections import deque
from typing import List

class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        result = []
        for right in range(n):
            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()
            queue.append(right)
            left = right - k + 1
            if queue[0] < left:
                queue.popleft()
            if right >= k - 1:
                result.append(nums[queue[0]])
        return result
