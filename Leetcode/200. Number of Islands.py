"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # (0, 0), (0, 1), (1, 0)
        # O(rows * cols)

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        if rows == 0 or cols == 0:
            return 0

        def dfs(r, c):
            if grid[r][c] == '0' or (r, c) in visited:
                return 0
            visited.add((r, c))
            for dr, dc in direction:
                if ((r + dr, c + dc) not in visited and
                        (r + dr) in range(rows) and
                        (c + dc) in range(cols) and
                        grid[r + dr][c + dc] == '1'):
                    dfs(r + dr, c + dc)

        result = 0
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == '1' and (r, c) not in visited):
                    dfs(r, c)
                    result += 1

        return result