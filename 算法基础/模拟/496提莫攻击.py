from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(1, len(timeSeries)):
            tmp = timeSeries[i] - timeSeries[i - 1]
            if tmp >= duration:
                ans += duration
            else:
                ans += tmp

        return ans + duration


print(Solution().findPoisonedDuration([1, 4], 2))
print(Solution().findPoisonedDuration([1, 2], 2))
