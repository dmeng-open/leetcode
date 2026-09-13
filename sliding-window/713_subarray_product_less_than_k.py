from typing import List


class Solution:
    def num_subarray_product_less_than_k(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        n = len(nums)
        product = 1
        result = 0
        left = 0
        for right in range(n):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            result += right - left + 1
        return result
            