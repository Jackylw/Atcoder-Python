from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(first=0):
            # 从第一层开始填，如果填完了，添加一个结果
            if first == n:
                ans.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # 撤销
                nums[first], nums[i] = nums[i], nums[first]
        backtrack()
        return ans