from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        max_count = 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    # 回收 left 窗口
                    k += 1
                left += 1
            max_count = max(max_count, right - left + 1)
            right += 1
        return max_count

