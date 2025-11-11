from typing import List

# 法一
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        使用双指针技术移动零：
        - left指针指向下一个非零元素应该放置的位置
        - right指针遍历数组寻找非零元素
        """
        left = 0  # 指向下一个非零元素应该放置的位置

        # 遍历数组，将所有非零元素移到前面
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        # 将剩余位置全部设置为0
        for i in range(left, len(nums)):
            nums[i] = 0

# 法二
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        使用双指针和交换思想：
        - left指针指向下一个非零元素应该放置的位置
        - right指针遍历数组寻找非零元素
        - 当找到非零元素时，与left位置的元素交换
        """
        left = 0  # 指向下一个非零元素应该放置的位置

        # 遍历数组，将所有非零元素交换到前面
        for right in range(len(nums)):
            if nums[right] != 0:
                # 交换 nums[left] 和 nums[right]
                nums[left], nums[right] = nums[right], nums[left]
                left += 1