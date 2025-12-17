from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        # i,j点处的最小下降和
        dp = [[0] * cols for _ in range(rows)]
        # 初始化第一行
        for i in range(cols):
            dp[0][i] = matrix[0][i]

        # 从第二行开始，因为第一行已经初始化了
        for i in range(1, rows):
            for j in range(cols):
                candidates = []
                if j - 1 >= 0:
                    candidates.append(dp[i - 1][j - 1])
                candidates.append(dp[i - 1][j])
                if j + 1 < cols:
                    candidates.append(dp[i - 1][j + 1])

                dp[i][j] = min(candidates) + matrix[i][j]

        return min(dp[rows - 1])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(Solution().minFallingPathSum(matrix))
matrix2 = [[-19,57],[-40,-5]]
print(Solution().minFallingPathSum(matrix2))
