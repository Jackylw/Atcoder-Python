from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = [[-1] * n for _ in range(m)]

        # 统计陆地并初始化队列
        land_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land_count += 1
                    visited[i][j] = 0
                    q.append((i, j))

        # 边界情况：全陆地或全海洋
        if land_count == 0 or land_count == m * n:
            return -1

        max_dist = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 多源 BFS
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    max_dist = visited[nx][ny]  # BFS 层序，最后赋值即最大
                    q.append((nx, ny))

        return max_dist