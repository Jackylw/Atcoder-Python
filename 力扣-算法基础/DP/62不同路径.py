class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp 含义：到达坐标 m，n 处的路径数
        # 注意 起点在 1,1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = 1
        # dp[0][1] = 1
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not (i == 1 and j == 1):
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


print(Solution().uniquePaths(3, 7))
