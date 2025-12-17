from typing import List


class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        rows = len(frame)
        cols = len(frame[0])
        # 设立 dp 数组，dp[i][j]代表到达这个柜子的最高价值
        # 起点 [1][1]
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        dp[1][1] = frame[0][0]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + frame[i - 1][j - 1]
        return dp[rows][cols]

frame = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().jewelleryValue(frame))
