from typing import List


class Solution:
    def car_pooling(self, trips: List[List[int]], capacity: int) -> bool:
        deltas = [0] * 1001
        for count, start, end in trips:
            deltas[start] += count
            deltas[end] -= count
        count = 0
        for delta in deltas:
            count += delta
            if count > capacity:
                return False
        return True