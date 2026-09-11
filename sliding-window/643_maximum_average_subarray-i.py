from ast import List

# 1 <= k <= n
class Solution:
    def find_max_average(self, nums: List[int], k: int) -> float:
        n = len(nums)
        result = float('-inf')
        total = 0
        left = 0
        for right in range(n):
            total += nums[right]
            if right - left + 1 > k:
                total -= nums[left]
                left += 1
            if right - left + 1 == k:
                result = max(result, total)
        return result / k
 
    def find_max_average_v2(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = sum(nums[:k])
        result = total
        for right in range(k, n):
            delta = nums[right] - nums[right - k]
            total += delta
            result = max(result, total)
        return result / k   
