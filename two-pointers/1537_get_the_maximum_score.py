from typing import List

# T: O(m + n)
# S: O(1)
def max_sum(nums1: List[int], nums2: List[int]) -> int:
    a_idx = b_idx = sum1 = sum2 = 0
    while a_idx < len(nums1) or b_idx < len(nums2):
        if b_idx >= len(nums2):
            sum1 += nums1[a_idx]
            a_idx += 1
        elif a_idx >= len(nums1):
            sum2 += nums2[b_idx]
            b_idx += 1
        elif nums1[a_idx] < nums2[b_idx]:
            sum1 += nums1[a_idx]
            a_idx += 1
        elif nums1[a_idx] > nums2[b_idx]:
            sum2 += nums2[b_idx]
            b_idx += 1
        else:
            sum1 = sum2 = max(sum1, sum2) + nums1[a_idx]
            a_idx += 1
            b_idx += 1
    return max(sum1, sum2) % (10**9 + 7)
