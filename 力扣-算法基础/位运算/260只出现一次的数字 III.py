from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1

        for i in h:
            if h[i] == 1:
                ans.append(i)

        return ans

    def singleNumber2(self, nums: List[int]) -> List[int]:
        ans = 0
        # 由题目可知，出现两次的均被抵消
        for i in nums:
            ans ^= i
        # 此时 ans = a ^ b

        # 获取最右边的一位，这一位表示了 a，b 在这一位不同
        mask = ans & (-ans)
        a = 0
        # 利用 mask 将数组分为两组，一个是该位为 1，一个是该位为 0
        for i in nums:
            if i & mask:
                a ^= i
        return [a, ans ^ a]