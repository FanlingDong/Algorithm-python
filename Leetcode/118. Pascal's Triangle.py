"""

https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    [[1],
   [1,1],
  [1,2,1],
 [1,3,3,1],
[1,4,6,4,1]]


Example 2:

Input: numRows = 1
Output: [[1]]


"""


class Solution:
    def generate(self, numRows: int):
        res = []
        # i: 0 1 2 3 ... n - 1
        for i in range(numRows):
            # j: 0, 1, 2, ...i
            cur = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(cur)
        return res
