from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 递增
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            # 递减
            else:
                right = mid
        return right

s1 = Solution().peakIndexInMountainArray([0,1,0])
print(s1)
s2 = Solution().peakIndexInMountainArray([0,2,1,0])
print(s2)
s3 = Solution().peakIndexInMountainArray([0,10,5,2])
print(s3)