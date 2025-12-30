from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 分析
        # 1. 偷nums[0]就不偷nums[1] nums[n-1]
        # 2. 不偷nums[0] 就偷nums[1]到最后
        def rob1(nums):
            n = len(nums)
            dp = [0] * (n+2)
            for i in range(2, len(nums) + 2):
                dp[i] = max(dp[i-2] + nums[i-2], dp[i-1])
            return dp[n+1]

        return max(nums[0] + rob1(nums[2:-1]), rob1(nums[1:]))

nums = [2,3,2]
print(Solution().rob(nums))
