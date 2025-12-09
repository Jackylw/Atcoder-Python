class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 定义 f 二维表，(i,j)代表数字 i 到 j 之间所需要花费的最小金额
        # 目标为求 f(1,n)
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                # 假设先猜最大值 j,猜错,作为初始上界
                f[i][j] = j + f[i][j - 1]
                # 猜中间的 K
                for k in range(i, j):
                    f[i][j] = min(f[i][j], k + max(f[i][k - 1], f[k + 1][j]))
        return f[1][n]