from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 在数组中找一个最长连续子数组，其和为 total - x
        total = sum(nums)
        n = len(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return n

        # 滑动窗口
        left = 0
        current_sum = 0
        max_len = -1

        for i in range(n):
            current_sum += nums[i]
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, i - left + 1)
        return n - max_len if max_len != -1 else -1
