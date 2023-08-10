"""

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 0-9 10进制
        # A - Z 是 1 - 26， 26进制

        dict = {}

        for i in range(1, 27):
            dict[chr(ord('A') + i - 1)] = i

        n = len(columnTitle)
        res = 0
        s = columnTitle[::-1]
        for i in range(n):
            res += dict[s[i]] * (26**i)
        return res