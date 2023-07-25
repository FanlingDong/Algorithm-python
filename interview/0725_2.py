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
# (1, 1) -> [(2, 3), (3, 2)] -> (4, 4)
# dp[1, 1] = 1
# dp[2, 3] = 1
# dp[3, 2] = 1
# dp[4, 4] = dp
# dp[i, j] = dp[i-1,j-2] + dp[i-2, j-1]
def main(n: int, m: int) -> int:
    # 1,1 1,2 1,3 1,4
    # 2,1 1 1
    # 3,1
    #              4,4
    result = 0
    start_i = 1
    start_j = 1

    pass


main(4, 4)