# Last updated: 4/4/2026, 10:24:05 AM
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
        
class Solution:
    def lengthOfLastWord(self , s: str) -> int:
        
      s = s.strip()  #clear spaces

      words = s.split() #make single string into multiple words. 

      return len(words[-1])