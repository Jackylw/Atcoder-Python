from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 可理解为除开自己本身，其他元素的积
        n = len(nums)
        ans_left = []
        ans_right = []
        ans = []

        # 左前前缀积
        for i in range(n):
            if i == 0:
                ans_left.append(nums[i])
            else:
                ans_left.append(nums[i] * ans_left[i - 1])

        # 右后缀积
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                ans_right.append(nums[i])
            else:
                ans_right.append(nums[i] * ans_right[-1])
        ans_right.reverse()

        for i in range(n):
            if i == 0:
                ans.append(ans_right[i + 1])
            elif i == n - 1:
                ans.append(ans_left[i - 1])
            else:
                ans.append(ans_left[i - 1] * ans_right[i + 1])
        return ans


s1 = Solution().productExceptSelf([1, 2, 3, 4])
print(s1)
s2 = Solution().productExceptSelf([-1, 1, 0, -3, 3])
print(s2)
