from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        # 起点或者终点为障碍物
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        dp[1][1] = 1
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if i == 1 and j == 1:
                    continue
                # 检查当前格子
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[rows][cols]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))

