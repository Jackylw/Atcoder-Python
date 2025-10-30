from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        tmp = 0
        for i in nums:
            tmp ^= i

        # 此时得到的 tmp 为 a ^ b
        for i in range(1, len(nums) + 3):
            tmp ^= i

        mask = tmp & (-tmp)

        x = 0
        # 分类
        for i in nums:
            if i & mask:
                x ^= i
        for i in range(1, len(nums) + 3):
            if i & mask:
                x ^= i
        return [x, tmp ^ x]
