from typing import List


class Solution:
    # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        # 已经走过的地方归零
        def dfs(grid, i, j):
            grid[i][j] = 0
            for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == "1":
                    dfs(grid, m, n)

        nr = len(grid)
        nc = len(grid[0])
        if nr == 0:
            return 0

        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1

        return count

    # BFS_DFS
    def numIslands2(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    queue = [(r, c)]
                    grid[r][c] = 0
                    # 把连通的地方置为 0
                    while queue:
                        row, col = queue.pop(0)
                        for m, n in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= m < rows and 0 <= n < cols and grid[m][n] == "1":
                                queue.append((m, n))
                                grid[m][n] = 0

        return count
