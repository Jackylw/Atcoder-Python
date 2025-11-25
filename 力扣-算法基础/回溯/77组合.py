from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(start):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                # 剪枝优化，剩余的数字数量不足k-len(path)，则不需要递归
                if n - i + 1 < k - len(path):
                    break
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res


print(Solution().combine(4, 2))
