from typing import List


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        计算到达楼梯顶部的最小花费。

        思路：
        - 楼梯有 n 个台阶，编号为 0 到 n-1。
        - 楼顶在台阶 n（即数组之外）。
        - 每次可以从台阶 i 支付 cost[i] 后，跳到 i+1 或 i+2。
        - 可以从台阶 0 或 1 开始（意味着初始站在 0 或 1 时就要支付对应费用）。
        - 目标：用最少总花费到达台阶 n（楼顶）。

        状态定义：
        dp[i] 表示「站在第 i 个台阶上，并已支付 cost[i]」时的最小累计花费。

        转移方程：
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        最终答案：
        因为从台阶 n-1 或 n-2 都可以直接一步到楼顶（无需再付费），
        所以答案是 min(dp[n-1], dp[n-2])
        """
        n = len(cost)

        # 边界情况：至少有两个台阶（题目保证）
        if n == 1:
            return cost[0]  # 实际不会出现，但安全起见
        if n == 2:
            return min(cost[0], cost[1])

        # 初始化：站在第 0 阶和第 1 阶的花费
        prev2 = cost[0]  # dp[0]
        prev1 = cost[1]  # dp[1]

        # 从第 2 阶开始递推到第 n-1 阶
        for i in range(2, n):
            current = min(prev1, prev2) + cost[i]
            # 滚动更新：prev2 <- prev1, prev1 <- current
            prev2, prev1 = prev1, current

        # 到达楼顶前最后可能站在 n-2 或 n-1 阶，选花费更小的
        return min(prev1, prev2)

cost1 = [10,15,20]
print(Solution().minCostClimbingStairs(cost1))
cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution().minCostClimbingStairs(cost))