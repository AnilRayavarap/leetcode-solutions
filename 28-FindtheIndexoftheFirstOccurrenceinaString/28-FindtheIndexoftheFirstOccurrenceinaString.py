# Last updated: 1/10/2026, 2:29:05 PM
1class Solution:
2    def strStr(self , haystack:str , neddle:str) -> int:
3        if neddle == "":
4            return 0
5        for i in range(len(haystack) + 1 - len(neddle)):
6            for j in range(len(neddle)):
7                if haystack[i+j] != neddle[j]:
8                    break
9                if j == len(neddle) - 1:
10                    return i
11        return -1
12
13