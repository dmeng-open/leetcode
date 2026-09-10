from typing import List

# O(n) | O(1)
def max_profit(prices: List[int]) -> int:
    n = len(prices)
    i = 0
    result = 0
    for j in range(n):
        if prices[j] < prices[i]:
            i = j
        result = max(result, prices[j] - prices[i])
    return result