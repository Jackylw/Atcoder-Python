from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while right > left:
            tmp = min(height[left], height[right]) * abs(right - left)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
            ans = max(ans, tmp)
        return ans