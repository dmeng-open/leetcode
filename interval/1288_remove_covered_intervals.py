from typing import List


class Solution:
    def remove_covered_intervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            top = stack[-1]
            top_start = top[0]
            top_end = top[-1]
            # 应为排序，当前区间最小就是等于栈顶区间，不可能小于
            if start == top_start: # [1, 2] <- [1, 3] 栈顶区间被当前区间合并
                if end > top_end:
                    stack[-1] = intervals[i]
                # [1, 5] <- [1, 2] 当前区间被栈顶区间合并，什么都不干
            elif end > top_end: # [1, 3] <- [2, 4]
                stack.append([start, end])
            # [1, 3] <- [2, 3] 当前区间被栈顶区间合并，什么都不干
        return len(stack)