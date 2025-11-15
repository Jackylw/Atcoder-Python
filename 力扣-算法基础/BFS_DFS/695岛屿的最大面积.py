from typing import List


class Solution:

    def dfs(self, grid, i, j) -> int:
        grid[i][j] = 0
        sum = 1
        for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == 1:
                sum += self.dfs(grid, m, n)
        return sum

    # DFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))

        return max_area

    def bfs(self, grid, i, j) -> int:
        grid[i][j] = 0
        sum = 1
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == 1:
                    grid[m][n] = 0
                    sum += 1
                    queue.append((m, n))
        return sum

    # BFS_DFS
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.bfs(grid, i, j))

        return max_area


gird = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(Solution().maxAreaOfIsland(gird))
print(Solution().maxAreaOfIsland2(gird))
