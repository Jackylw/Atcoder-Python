from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0

        def backtrack(index, cur_sum, path):
            nonlocal count
            if index == len(nums):
                if cur_sum == target:
                    count += 1
                return

            path.append(nums[index])
            backtrack(index + 1, cur_sum + nums[index], path)
            path.pop()

            path.append(-nums[index])
            backtrack(index + 1, cur_sum - nums[index], path)
            path.pop()

        backtrack(0, 0, [])
        return count

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < target or (target + total) % 2:
            return 0
        subset_sum = (target + total) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(subset_sum, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[subset_sum]


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
