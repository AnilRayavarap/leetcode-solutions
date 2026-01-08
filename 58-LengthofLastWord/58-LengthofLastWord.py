# Last updated: 1/7/2026, 11:43:23 PM
1# class Solution:
2#     def lengthOfLastWord(self, s: str) -> int:
3        
4class Solution:
5    def lengthOfLastWord(self , s: str) -> int:
6        
7      s = s.strip()  #clear spaces
8
9      words = s.split() #make single string into multiple words. 
10
11      return len(words[-1])