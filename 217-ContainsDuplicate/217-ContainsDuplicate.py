# Last updated: 4/6/2026, 9:44:35 AM
1# class Solution:
2#     def containsDuplicate(self,
3#  nums: List[int]) -> bool:
4        
5
6class Solution:
7    def containsDuplicate(self , nums:List[int]) -> bool:
8        
9        values = set()
10        for num in nums:
11            if num in values:
12                return True
13            values.add(num)
14            
15        return False