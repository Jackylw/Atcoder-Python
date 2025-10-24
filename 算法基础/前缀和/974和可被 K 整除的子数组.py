from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 0
        h = {0: 1}

        for i in range(len(nums)):
            total += nums[i]
            mod = total % k
            same = h.get(mod, 0)
            ans += same
            h[mod] = same + 1

        return ans
            