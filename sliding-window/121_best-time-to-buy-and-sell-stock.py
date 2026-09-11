from typing import List

# 1 <= len(prices) <= 10^5
# 0 <= price <= 10^4
# 7 1 0 3 10^4 4
#     l
#                r
class Solution:
    def max_profit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        left = 0
        for right in range(n):
            # 有效窗口的条件：从左边界递增才可能产生利润
            if prices[right] < prices[left]:
                left = right
            else:
                result = max(result, prices[right] - prices[left])
        return result