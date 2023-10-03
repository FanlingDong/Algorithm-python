"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0


Constraints:

0 <= num <= 231 - 1


Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum_ = 0
            while num:
                sum_ += num % 10
                num  = num // 10
            num = sum_
        return num

s = Solution()
print(s.addDigits(38))


class Solution2:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        return num % 9 or 9


"""
return num % 9 or 9：对于非零的 num，这行代码计算其各位数字相加的结果。这是根据数字根的性质得到的。
数字根是一个介于1到9之间的结果，表示将一个多位数的各位数字相加，直到得到一个一位数为止。

num % 9 计算了 num 除以9的余数。这是因为当 num 为9的倍数时，其各位数字相加结果为9，而不是0。
所以我们需要检查余数，如果余数为0，就返回9，否则返回余数。

使用 or 运算符是为了处理 num 为9的倍数的情况，因为在这种情况下 num % 9 会返回0，而我们需要返回9。
"""