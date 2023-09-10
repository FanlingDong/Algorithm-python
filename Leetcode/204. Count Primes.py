"""
Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0


Constraints:

0 <= n <= 5 * 106
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        # 一个非质数一定有一个因子小于或等于它的平方根。
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # 将i和i倍的数字都标记为True
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)