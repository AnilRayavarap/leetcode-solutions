# Last updated: 11/8/2025, 2:13:59 AM
class Solution:
    def removeElement(self , nums , val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i = i + 1
        return i