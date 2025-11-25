from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        path = []

        # 求子集
        def backtrack(start=0):
            subsets.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack()

        # 求子集异或和
        ans = 0

        def xor_sum(subset):
            xor = 0
            for num in subset:
                xor ^= num
            return xor

        for subset in subsets:
            ans += xor_sum(subset)

        return ans

    def subsetXORSum2(self, nums: List[int]) -> int:
        ans = 0
        path = []

        def backtrack(start=0, xor=0):
            nonlocal ans
            ans += xor

            for i in range(start, len(nums)):
                path.append(nums[i])
                cur_xor = xor ^ nums[i]
                backtrack(i + 1, cur_xor)
                path.pop()

        backtrack()
        return ans
