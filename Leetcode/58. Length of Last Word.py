"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while s[end] == ' ':
            end -= 1
        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1
        return end - start


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
      list = s.split(' ')
      res = 0
      for i in list[::-1]:
        if i != '':
          res = len(i)
          break

      return res