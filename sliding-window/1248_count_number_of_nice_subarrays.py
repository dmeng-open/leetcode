from typing import List


class Solution:
    def number_of_subarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def odd(num: int) -> bool:
            return num % 2 != 0

        def lte(k: int) -> int:
            count = 0
            left = 0
            result = 0
            for right in range(n):
                count += odd(nums[right])
                while count > k:
                    count -= odd(nums[left])
                    left += 1
                result += right - left + 1
            return result

        return lte(k) - lte(k - 1)