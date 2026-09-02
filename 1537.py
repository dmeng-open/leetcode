from typing import List

# T: O(m + n)
# S: O(1)
class Solution:
    def get_the_max_score(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = sum1 = sum2 = 0
        while i < len(nums1) or j < len(nums2):
            if j >= len(nums2):
                sum1 += nums1[i]
                i += 1
            elif i >= len(nums1):
                sum2 += nums2[j]
                j += 1
            elif nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
        return max(sum1, sum2) % (10**9 + 7)