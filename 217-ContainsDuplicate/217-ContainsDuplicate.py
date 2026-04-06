# Last updated: 4/6/2026, 9:45:43 AM
1# class Solution:
2#     def containsDuplicate(self,
3#  nums: List[int]) -> bool:
4        
5
6class Solution:
7    def containsDuplicate(self , nums:List[int]) -> bool:
8        return len(nums) != len(set(nums))