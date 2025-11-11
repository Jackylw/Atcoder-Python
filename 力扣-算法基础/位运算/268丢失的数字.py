from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums  = sorted(nums)
        n = len(nums)
        nums_check = []
        for i in range(n + 1):
            nums_check.append(i)

        for i in range(n):
            if sorted_nums[i] != nums_check[i]:
                return nums_check[i]
        return n

    def missingNumber2(self, nums: List[int]) -> int:
        ans = 0
        # 异或运算性质，出现过的数字两次异或会抵消掉
        for i in nums:
            ans ^= i
        for i in range(len(nums) + 1):
            ans ^= i
        return ans