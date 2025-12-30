from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 反向 dp
        # dp[i][j] 表示：从 (i, j) 出发，走到终点所需的最小初始血量。
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        # 起点是 rows-1,cols-1
        # 终点的右下为 1，从终点反向计算
        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, need - dungeon[i][j])
        return dp[0][0]


d1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(Solution().calculateMinimumHP(d1))
