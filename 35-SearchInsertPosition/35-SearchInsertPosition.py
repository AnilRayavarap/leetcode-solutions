# Last updated: 11/16/2025, 1:27:34 AM
class Solution:
    def searchInsert(self , nums , target):
        for i , num in enumerate(nums):
            if num  >= target:
                return i
            
        return len(nums)