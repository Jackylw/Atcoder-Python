from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 旋转，即向右平移一次，nums 变为两个单增序列，且第一个单增序列均大于第二个单增序列
        left = 0
        right = len(nums) - 1
        x = nums[-1]
        while left < right:
            mid = left + (right - left) // 2
            # 中间值大于最右，则旋转点在 mid 的右侧
            if nums[mid] > x:
                left = mid + 1
            else:
                right = mid
        return nums[left]
