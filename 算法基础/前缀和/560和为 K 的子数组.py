from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 假设 total[i] 为 nums 的前缀和
        # 查找起始位置 x 的区间和为
        # total[i] - total[x-1] = k
        # 满足以上式子即为一个子数组
        # 所以有 total[x-1] = total[i] - k
        ans = 0
        total = 0
        h = {0: 1}

        for i in range(len(nums)):
            total += nums[i]

            # 查看是否有前缀和等于 total - k
            target = total - k
            if target in h:
                ans += h[target]

            # 更新前缀和出现的次数
            h[total] = h.get(total, 0) + 1

        return  ans
