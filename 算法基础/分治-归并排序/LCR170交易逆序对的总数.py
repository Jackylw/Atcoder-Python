from typing import List

class Solution:
    # 归并


    def reversePairs(self, record: List[int]) -> int:


    # 暴力
    def reversePairs2(self, record: List[int]) -> int:
        ans = []
        for i in range(len(record)):
            for j in range(i + 1, len(record)):
                if record[i] > record[j]:
                    ans.append([record[i], record[j]])

        return len(ans)
