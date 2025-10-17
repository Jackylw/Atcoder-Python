from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_count = arr.count(0)
        left = len(arr) - 1  # 指向数组的最后一位，从后往前读
        right = len(arr) - 1 + zero_count  # 指向扩展数组的最后一位
        while left >= 0:
            # 右指针在有效范围内，才写入
            if right < len(arr):
                arr[right] = arr[left]

            if arr[left] == 0:
                right -= 1
                if right < len(arr):
                    arr[right] = 0

            left -= 1
            right -= 1
