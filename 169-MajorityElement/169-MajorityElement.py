# Last updated: 1/16/2026, 1:59:32 PM
1class Solution:
2    def majorityElement(self, nums):
3        n = len(nums)
4        count = {}
5        i = 0
6        while i < n:
7            num = nums[i]
8            if num in count:
9                count[num] += 1
10            else:
11                count[num] = 1
12            
13            if count[num] > n / 2:
14                return num
15
16            i += 1