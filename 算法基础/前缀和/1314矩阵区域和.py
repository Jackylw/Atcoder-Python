from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m ,n = len(mat), len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + mat[i - 1][j - 1]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1, y1 = max(0, i - k), max(0, j - k)
                x2, y2 = min(m, i + k + 1), min(n, j + k + 1)
                ans[i][j] = pre[x2][y2] - pre[x1][y2] - pre[x2][y1] + pre[x1][y1]

        return ans