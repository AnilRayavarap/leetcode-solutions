# Last updated: 4/4/2026, 10:24:07 AM
class Solution:
    def strStr(self , haystack:str , neddle:str) -> int:
        if neddle == "":
            return 0
        for i in range(len(haystack) + 1 - len(neddle)):
            for j in range(len(neddle)):
                if haystack[i+j] != neddle[j]:
                    break
                if j == len(neddle) - 1:
                    return i
        return -1

