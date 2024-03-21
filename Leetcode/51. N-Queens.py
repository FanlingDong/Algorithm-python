"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""


class Solution:
    def __init__(self):
        # 三维数组
        self.result = []

    def solveNQueens(self, n: int):
        chess_board = ['.' * n for _ in range(n)]
        self.backTracking(n, chess_board, 0, self.result)
        return [[''.join(row) for row in solution] for solution in self.result]

    def backTracking(self, n: int, chess_board, row, result):
        # 到了叶子节点，不合法的结果在走这步之前就被卡掉了
        if row == n:
            result.append(chess_board[:])
            return

        for col in range(n):
            if self.isValid(row, col, chess_board):
                # 放置皇后
                chess_board[row] = chess_board[row][:col] + "Q" + chess_board[row][col + 1:]
                self.backTracking(n, chess_board, row+1, result)
                # 回溯
                chess_board[row] = chess_board[row][:col] + '.' + chess_board[row][col + 1:]

    def isValid(self, row, col, chess_board):
        # 检查列有无皇后
        for i in range(row):
            if chess_board[i][col] == 'Q':
                return False

        # 检查45度角有无皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chess_board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # 检查135度有无皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chess_board):
            if chess_board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True


s = Solution()
print(s.solveNQueens(4))