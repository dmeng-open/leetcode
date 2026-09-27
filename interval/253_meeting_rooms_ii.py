from typing import List


class Solution:
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        max_end = max(end for start, end in intervals)
        deltas = [0] * (max_end + 1)
        for start, end in intervals:
            deltas[start] += 1
            deltas[end] -= 1
        active = max_active = 0
        for delta in deltas:
            active += delta
            max_active = max(max_active, active)
        return max_active