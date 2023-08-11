"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}

        for c in s:
            dict[c] = 1 + dict.get(c, 0)

        for key, value in dict.items():
            if value == 1:
                return s.index(key)
        return -1