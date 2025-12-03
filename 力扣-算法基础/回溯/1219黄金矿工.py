from typing import List


class Solution:
    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or visited[i][j]:
            return 0

        visited[i][j] = True
        current_gold = grid[i][j]
        max_gold = 0

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            max_gold = max(max_gold, self.dfs(grid, i + di, j + dj, visited))

        visited[i][j] = False

        return current_gold + max_gold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        max_gold = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, self.dfs(grid, i, j, visited))

        return max_gold


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
grid2 = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]

print(Solution().getMaximumGold(grid))
print(Solution().getMaximumGold(grid2))
