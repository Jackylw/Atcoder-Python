from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(0, n):
            if nums[i] == nums[i - 1] and i > 0:
                 continue
            # 每次固定位置 i 的数
            # 剩下两数在 i+1 和 n-1 之间找
            left = i + 1
            right = n - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 去重
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
        return ans
