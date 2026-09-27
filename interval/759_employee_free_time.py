import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

# 用没处理的 intervals 的全局最小（用 heap 来 k 路归并）和已经处理的全局覆盖最远的作比较
# O(nlog(k)) | O(k)
class Solution:
    def employee_free_time(self, schedule: [[Interval]]) -> [[Interval]]: # type: ignore
        result = []
        heap = []
        for employee_index, intervals in enumerate(schedule):
            if intervals:
                heapq.heappush(heap, (intervals[0].start, employee_index, 0))
        max_end = heap[0][0]
        while heap:
            interval_start, employee_index, interval_index = heapq.heappop(heap)
            if interval_start > max_end:
                result.append(Interval(max_end, interval_start))
            intervals = schedule[employee_index]
            interval = intervals[interval_index]
            max_end = max(max_end, interval.end)
            next_interval_index = interval_index + 1
            if next_interval_index < len(intervals):
                next_interval = intervals[next_interval_index]
                heapq.heappush(heap, (next_interval.start, employee_index, next_interval_index))
        return result