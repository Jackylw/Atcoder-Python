from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        # 太平洋边界
        pacific_queue = deque()
        for i in range(row):
            pacific_queue.append((i, 0))
            pacific_reachable.add((i, 0))
        for j in range(col):
            pacific_queue.append((0, j))
            pacific_reachable.add((0, j))

        # 大西洋边界
        atlantic_queue = deque()
        for i in range(row):
            atlantic_queue.append((i, col - 1))
            atlantic_reachable.add((i, col - 1))
        for j in range(col):
            atlantic_queue.append((row - 1, j))
            atlantic_reachable.add((row - 1, j))

        # BFS
        def bfs(queue, reachable):
            while queue:
                x, y = queue.popleft()
                for m, n in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= m < row and 0 <= n < col and (m, n) not in reachable and heights[m][n] >= heights[x][y]:
                        reachable.add((m, n))
                        queue.append((m, n))

        # 双向 bfs
        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)

        return [[x, y] for (x, y) in pacific_reachable & atlantic_reachable]


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(Solution().pacificAtlantic(heights))
