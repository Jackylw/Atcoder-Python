from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left_tmp = mid
                right_tmp = mid
                while left_tmp >= 0 and nums[left_tmp] == target:
                    left_tmp -= 1
                while right_tmp < len(nums) and nums[right_tmp] == target:
                    right_tmp += 1
                return [left_tmp + 1, right_tmp - 1]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]

s1 = Solution().searchRange([5,7,7,8,8,10], 8)
print(s1)
s2 = Solution().searchRange([5,7,7,8,8,10], 6)
print(s2)
s3 = Solution().searchRange([], 0)
print(s3)