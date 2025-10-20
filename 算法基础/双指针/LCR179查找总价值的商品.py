from typing import List


class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        left = 0
        right = len(price) - 1
        while left < right:
            if price[left] + price[right] == target:
                return [price[left], price[right]]
            elif price[left] + price[right] > target:
                right -= 1
            else:
                left += 1
