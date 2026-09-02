class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 0
        size = len(nums)

        while j < size:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1

        return i + 1