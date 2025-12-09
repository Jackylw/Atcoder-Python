from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        # i,j 处最长递增路径长度
        dp = [[-1] * cols for _ in range(rows)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            max_path = 1  # 至少包含自己
            for dx, dy in direction:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                    path_len = 1 + dfs(x, y)
                    max_path = max(max_path, path_len)
            dp[i][j] = max_path
            return max_path

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))

        return ans

print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))