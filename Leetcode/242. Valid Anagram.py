"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 数组法就是用数组当dict，索引是从a到z的offset

        record = [0] * 26
        if len(s) != len(t): return False
        for i in s:
            record[ord(i)-ord('a')] += 1
        for i in t:
            record[ord(i)-ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        char = {}
        for string in s:
            if string not in char:
                char[string] = 1
            else:
                char[string] += 1
        for target in t:
            if target in char:
                char[target] -= 1
            else:
                return False

        for key, value in char.items():
            if value != 0:
                return False
        return True