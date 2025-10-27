from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h = {0: -1}
        ans = 0
        total = 0

        for i in range(len(nums)):
            total += -1 if nums[i] == 0 else 1
            if total in h:
                ans = max(ans, i - h[total])
            else:
                h[total] = i

        return ans
