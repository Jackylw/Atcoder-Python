from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # i,j代表 dp 该点的最小路径和，起点 1，1
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if i == 1 and j == 1:
                    continue
                # 在第一行
                if i - 1 == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i - 1][j - 1]
                # 在第一列
                elif j - 1 == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[rows][cols]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(grid))
grid2 = [[1,2,3],[4,5,6]]
print(Solution().minPathSum(grid2))

