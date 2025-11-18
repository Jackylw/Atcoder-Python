from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        dist = [[-1] * col for _ in range(row)]
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            # 多源BFS，逐个计算距离扩展
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < row and 0 <= ny < col and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        return dist

print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))