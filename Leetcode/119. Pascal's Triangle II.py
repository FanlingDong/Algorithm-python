"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

# easy understand
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []

        for i in range(rowIndex + 1):
            res.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        return res[rowIndex]


# best
class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        if rowIndex == 0: return row
        prev_row = self.getRow(rowIndex-1)

        for i in range(1, len(row) - 1):
            row[i] = prev_row[i-1] + prev_row[i]

        return row