from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        rows = len(costs)
        cols = len(costs[0])
        # 第 i 个房子的 j 颜色的最小开销
        dp = [[0] * cols for _ in range(rows)]

        for j in range(cols):
            dp[0][j] = costs[0][j]

        for i in range(1, rows):
            for j in range(cols):
                dp[i][j] = costs[i][j] + min(
                    dp[i - 1][k] for k in range(cols) if k != j
                )

        return min(dp[rows - 1])


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(Solution().minCost(costs))
