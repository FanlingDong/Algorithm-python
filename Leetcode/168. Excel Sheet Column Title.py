"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 231 - 1
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 26 进制， 除26倒取余法
        # A->Z: 1 - 26
        # 701 / 26 = 26 ... 25
        #  col       res   remainder
        # 25 / 26 = 0 ... 25

        # res = ""

        # while columnNumber > 0:
        #     remainder = (columnNumber - 1) % 26
        #     print(remainder, columnNumber)
        #     res = chr(65 + remainder) + res
        #     columnNumer = (columnNumber - 1) // 26
        # return res

        result = ""
        num = columnNumber
        while num > 0:
            remainder = (num - 1) % 26
            result = chr(65 + remainder) + result  # 65是字符'A'的ASCII码
            num = (num - 1) // 26
        return result



