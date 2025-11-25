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

    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []  # 存放当前路径
        used = [False] * len(nums)  # 标记数字是否使用

        def backtrack(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                # 跳过已经使用的数字
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(nums)
                # 回溯
                path.pop()
                used[i] = False

        backtrack(nums)
        return res
