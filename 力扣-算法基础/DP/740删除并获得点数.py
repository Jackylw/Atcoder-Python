from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def rob(nums):
            n = len(nums)
            dp = [0] * (n + 2)
            for i in range(2, len(nums) + 2):
                dp[i] = max(dp[i - 2] + nums[i - 2], dp[i - 1])
            return dp[n + 1]

        a = [0] * (max(nums) + 1)
        for num in nums:
            a[num] += num

        return rob(a)


nums = [3, 4, 2]
print(Solution().deleteAndEarn(nums))

nums2 = [2,2,3,3,3,4]
print(Solution().deleteAndEarn(nums2))
