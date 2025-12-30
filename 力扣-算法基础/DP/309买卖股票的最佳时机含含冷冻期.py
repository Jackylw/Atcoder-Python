from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # dp[i][j] 第 i 天股票进行 j 操作后的最大利润
        # j-0:持有股票 j-1:不持有股票且处于冷冻期 j-2:不持有股票且不处于冷冻期
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = -prices[0] # 第一天买入股票
        dp[0][1] = 0          # 第一天不持有股票且处于冷冻期
        dp[0][2] = 0          # 第一天不持有股票且不处于冷冻期
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i]) # 持有股票
            dp[i][1] = dp[i - 1][0] + prices[i]                    # 不持有股票且处于冷冻期
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])             # 不持有股票且不处于冷冻期
        return max(dp[-1][1], dp[-1][2]) # 最后一天不持有股票的最大利润

prices =  [1,2,3,0,2]
print(Solution().maxProfit(prices))  # Output: 3
