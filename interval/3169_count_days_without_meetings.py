from typing import List


class Solution:
    def count_days(self, days: int, meetings: List[int]) -> int:
        count = last = 0
        meetings.sort()
        for start, end in meetings:
            if start > end:
                count += start - end - 1
            last = max(last, end)
        count += days - last
        return count