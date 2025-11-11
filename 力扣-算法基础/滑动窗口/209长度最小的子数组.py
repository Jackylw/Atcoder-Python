from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        res = float('inf')
        total = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                left += 1
                total -= nums[left - 1]
            right += 1
        if res == float('inf'):
            return 0
        else:
            return res


s1 = Solution().minSubArrayLen(4, [1, 4, 4])
print(s1)