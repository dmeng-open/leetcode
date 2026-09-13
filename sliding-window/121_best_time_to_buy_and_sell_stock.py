from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        left = 0
        for right in range(n):
            if prices[right] < prices[left]:
                left = right
            result = max(result, prices[right] - prices[left])
        return result 