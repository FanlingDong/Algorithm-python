"""
iven an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 104


Follow up: Could you write a solution that works in logarithmic time complexity?
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        count = 0
        while n != 0:
            n = n // 5
            count = count + n
        return count


# bad way
class Solution2:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i

        list_result = list(str(result))
        count = 0
        for i in list_result[::-1]:
            if i != '0':
                break
            else:
                count += 1
        return count

s = Solution()
print(s.trailingZeroes(7))