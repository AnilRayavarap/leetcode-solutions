# Last updated: 4/4/2026, 11:10:44 AM
1class Solution:
2    def groupAnagrams(self , strs):
3        anagram_map = {}
4        for word in strs:
5            key = ''.join(sorted(word))
6
7            if key not in anagram_map:
8                anagram_map[key] = []
9                # return True
10
11            anagram_map[key].append(word)
12
13        return list(anagram_map.values())
14
15
16