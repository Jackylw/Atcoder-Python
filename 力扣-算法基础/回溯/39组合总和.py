from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort() # 剪枝优化

        def backtrack(start, path, cur_sum):
            # 找到对应目标添加进 ans
            if cur_sum == target:
                ans.append(path[:])
                return
            # 超过目标直接剪枝
            if cur_sum > target:
                return
            # 尝试从 start 开始的每个候选数字
            for i in range(start, len(candidates)):
                num = candidates[i]
                # 由于已经排序，因此当前数字太大时，后面的一律不考虑
                if cur_sum + num > target:
                    break
                path.append(num)
                # i 不加 1，因为可以重复使用同一个数字
                backtrack(i, path, cur_sum + num)
                path.pop()

        backtrack(0, [], 0)
        return ans
