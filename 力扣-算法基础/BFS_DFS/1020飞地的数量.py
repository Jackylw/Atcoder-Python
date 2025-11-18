from typing import List
from collections import deque


class Solution:
    def bfs(self, grid: List[List[int]], x, y, count_area: bool):
        row = len(grid)
        col = len(grid[0])
        queue = deque([(x, y)])
        grid[x][y] = 0  # 初始点也要标记为0，避免重复计算
        area = 1 if count_area else 0  # 如果需要计算面积，初始点本身就是一块陆地
        while queue:
            x, y = queue.popleft()
            for m, n in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= m < row and 0 <= n < col and grid[m][n] == 1:
                    grid[m][n] = 0
                    queue.append((m, n))
                    if count_area:
                        area += 1
        return area

    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        # 邻边岛屿置 0
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    self.bfs(grid, i, j, False)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += self.bfs(grid, i, j, True)
        return ans


class Solution2:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visted = [[False] * n for _ in range(m)]
        q = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 多源 BFS 思路，将边界作为起点
        for i in range(m):
            for j in range(n):
                # 如果在陆地上
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    q.append((i, j))
                    visted[i][j] = True

        # 陆地边界扩散
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visted[nx][ny] and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    visted[nx][ny] = True

        # 此时未被访问的 1 节点即为要统计节点
        ans = 0
        for i in range(m):
            for j in range(n):
                if not visted[i][j] and grid[i][j] == 1:
                    ans += 1

        return ans


print(Solution2().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(Solution2().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
