from typing import List


class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        left = 0
        right = len(records) - 1
        while left < right:
            mid = left + (right - left) // 2
            if records[mid] == mid:  # 前一半没有缺失
                left = mid + 1
            else:
                right = mid
        # 如果列表中没有缺失的，那么说明最后一个缺失的索引为 len(records) + 1
        return left == records[left] and left + 1 or left
