from typing import Counter, List

# 如果 k 限于 26
# Counter 和 frequencies_reversed 的空间都是 O(26) = O(1)
# 排序的时间是 O(26log(26)) = O(1)
# Counter 的遍历时间是 O(n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies_reversed = sorted(Counter(tasks).values(), reversed=True)
        max_gaps = frequencies_reversed[0] - 1
        idle_slots = max_gaps * n
        for i in range(1, len(frequencies_reversed)): # O(1) 如果 k 限于 26
            frequency = frequencies_reversed[i]
            idle_slots_filled = min(max_gaps, frequency)
            idle_slots -= idle_slots_filled
            if idle_slots <= 0:
                return len(tasks)
        return len(tasks) + idle_slots