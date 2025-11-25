from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # 去重，如果当前元素和前一个相同，且前一个未被使用，则跳过
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return ans

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                ans.append(path.copy())
                return

            seen = set()

            for i in range(len(nums)):
                if used[i] or nums[i] in seen:
                    continue

                seen.add(nums[i])
                # 回溯
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return ans


print(Solution().permuteUnique([1, 1, 2]))
