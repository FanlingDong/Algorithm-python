"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 递归实现O(logn)的复杂度
        def pow_fn(base, recur):
            if recur == 0:
                return 1
            if recur == 1:
                return base
            t = pow_fn(base, recur // 2)
            if recur % 2 == 1:
                return t * t * base
            return t * t

        p = pow_fn(x, abs(n))
        return p if n > 0 else 1 / p

        # 复杂度为O(n)，太高了
        # power = 1
        # for i in range(abs(n)):
        #     power = x * power
        # if n < 0:
        #     power = 1 / power
        # return power

        # 用递归降低复杂度，复杂度依然是O(n)
        # def powFn(base, recur):
        #     if recur == 0:
        #         return 1
        #     if recur == 1:
        #         return base
        #     else:
        #         if recur % 2 == 0:
        #             return powFn(base, int(recur/2)) *  powFn(base, int(recur/2))
        #         else:
        #             return powFn(base, int(recur/2)) *  powFn(base, int(recur/2)) * x
        # f = powFn(x, abs(n))
        # return f if n > 0 else 1/f


