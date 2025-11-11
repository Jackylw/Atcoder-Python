from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        if n < 4:
            return []
        for i in range(n - 3):
            # 第一层去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                # 第二层去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1
                current_target = target - nums[i] - nums[j]

                while left < right:
                    current_sum = nums[left] + nums[right]
                    if current_sum > current_target:
                        right -= 1
                    elif current_sum < current_target:
                        left += 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        # 三层、四层去重
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
        return ans
