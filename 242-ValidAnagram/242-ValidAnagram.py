# Last updated: 4/4/2026, 10:23:43 AM
1# Approach 1.
2# class Solution:
3#     def isAnagram(self , s:str , t:str) -> bool:
4#         if len(s) != len(t):
5#             return false
6
7#         count = {}
8
9#         for char in s:
10#             count[char] = count.get(char , 0) + 1
11
12#         for char in t:
13#             if char not in count:
14#                 return False
15#             count[char] -= 1
16
17#             if count[char] < 0:
18#                 return False
19            
20#         return True
21
22#Aproach 2.
23class Solution:
24    def isAnagram(self , s:str , t:str):
25        return sorted(s) == sorted(t)