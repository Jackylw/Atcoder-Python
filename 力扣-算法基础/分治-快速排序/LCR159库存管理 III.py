from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        return sorted(stock)[:cnt]


print(Solution().inventoryManagement([0, 2, 3, 6], 2))
