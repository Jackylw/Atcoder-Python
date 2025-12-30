from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(2, n + 2):
            # 不选当前顾客、选当前顾客
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
        return dp[n + 1]
