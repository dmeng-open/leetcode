import heapq
from typing import List

# O(N log N + Q log Q) | O(N + Q)
class Solution:
    def min_interval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries_ordered = sorted((query, index) for index, query in enumerate(queries))
        result = [-1] * len(queries)
        heap = []
        interval_index = 0
        for  query, query_index in queries_ordered:
            # 把包括当前 query 的 intervals 入堆，按照 interval size 排序
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                size = end - start + 1
                heapq.heappush(heap, (size, end))
                interval_index += 1
            # 把堆中 end < query 的出堆
            while heap and heap[0][1] < query:
                heapq.pop(heap)
            if heap:
                size = heap[0][0]
                result[query_index] = size
        return result
            