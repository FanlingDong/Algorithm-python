"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""

import math

import math


class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            print(digit)
            x = int(x / 10)
            if res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10):
                return 0
            res = res * 10 + digit

        return res


s = Solution()
print(s.reverse(-1563847412))
