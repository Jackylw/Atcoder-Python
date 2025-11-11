from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = {}
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            # 将当前水果加入窗口
            fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

            # 如果水果类型超过2种，需要收缩窗口
            while len(fruit_count) > 2:
                # 移除窗口最左边的水果
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            # 更新最大水果数量
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

