# Knight
# You are given a N x M chessboard. On the top left of it, stands a chess knight.
# It can travel with the following moves:
# i + 1, j + 2
# i + 2, j + 1
# i - 1, j + 2
# i + 2, j - 1
# Determine how many different routes there are from top left to bottom right corner of the board.
# Example:
# Input::
# 4 4
# Output:
# 2
def main(n: int, m: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if 0 <= i + 1 < n and 0 <= j + 2 < m:
                dp[i + 1][j + 2] += dp[i][j]
            if 0 <= i + 2 < n and 0 <= j + 1 < m:
                dp[i + 2][j + 1] += dp[i][j]
            if 0 <= i - 1 < n and 0 <= j + 2 < m:
                dp[i - 1][j + 2] += dp[i][j]
            if 0 <= i + 2 < n and 0 <= j - 1 < m:
                dp[i + 2][j - 1] += dp[i][j]
    return dp[n - 1][m - 1]


print(main(4, 4))
