from typing import List
from collections import deque


class Solution:
    # 题目可理解为，距离 0 的最短长度
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        visited = [[-1] * col for _ in range(row)]
        q = deque()
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    visited[i][j] = 0

        while q:
            x, y = q.popleft()
            for m, n in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= m < row and 0 <= n < col and visited[m][n] == -1:
                    visited[m][n] = visited[x][y] + 1
                    q.append((m, n))

        return visited


print(Solution().highestPeak([[0, 1], [0, 0]]))
print(Solution().highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
