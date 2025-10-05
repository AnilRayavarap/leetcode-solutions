# Last updated: 10/5/2025, 8:46:47 AM
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
