# Knight
# You are given a N x M chessboard. On the top left of it, stands a chess knight.
# It can travel with the following moves:
# i + 1, j + 2
# i + 2, j + 1
# Determine how many different routes there are from top left to bottom right corner of the board.
# Example:
# Input::
# 4 4
# Output:
# 2

# Solution
# (1, 1) -> [(2, 3), (3, 2)] -> (4, 4)
# dp[1, 1] = 1
# dp[2, 3] = 1
# dp[3, 2] = 1
# dp[4, 4] = dp
# dp[i, j] = dp[i-1,j-2] + dp[i-2, j-1]


def main(n: int, m: int) -> int:
    # Init the 2D array to store the number of ways to reach each cell
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # Init the knight starts at the top left corner, so there is only 1 way to reach the call
    dp[0][0] = 1

    # Iterate through the chessboard
    for i in range(n):
        for j in range(m):

            # check if the knight can move to the cell (i+i, j+2):
            if (i + 1) < n and (j + 2) < m:
                dp[i + 1][j + 2] += dp[i][j]
            # check if the knight can move to the cell (i+2, j+1):
            if (i + 2) < n and (j + 1) < m:
                dp[i + 2][j + 1] += dp[i][j]

    # print(dp)
    # The result will be in the bottom right corner of the chessboard
    return dp[n - 1][m - 1]


print(main(4, 4))
