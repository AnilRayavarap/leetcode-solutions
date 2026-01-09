# Last updated: 1/8/2026, 11:51:09 PM
1class Solution:
2    def plusOne(self , digits : list[int]) -> list[int]:
3        n = len(digits)
4
5        for i in range(n):
6            reverse = n - i - 1
7
8            if digits[reverse] == 9:
9                digits[reverse] = 0
10            else:
11                digits[reverse] += 1
12                return digits
13        return [1] + digits