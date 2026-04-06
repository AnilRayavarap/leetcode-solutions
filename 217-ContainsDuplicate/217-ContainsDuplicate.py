# Last updated: 4/6/2026, 9:28:25 AM
1# class Solution:
2#     def containsDuplicate(self,
3#  nums: List[int]) -> bool:
4        
5
6class Solution:
7    def containsDuplicate(self , nums:List[int]) -> bool:
8        nums.sort()
9
10        n= len(nums) - 1
11        for i in range(n):
12            if nums[i] == nums[i+1]:
13                return True
14        return False