from typing import List


class Solution:
    def backtrack(self, grid, start_x, start_y):
        if grid[start_x][start_y] == 2:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        return 0
            return 1
        res = 0
        grid[start_x][start_y] = -1  # 标记为已访问
        for m, n in [(start_x - 1, start_y), (start_x + 1, start_y), (start_x, start_y - 1), (start_x, start_y + 1)]:
            if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and (grid[m][n] == 0 or grid[m][n] == 2): # 终点也可以走
                res += self.backtrack(grid, m, n)
        grid[start_x][start_y] = 0
        return res

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_x = i
                    start_y = j
                    ans = self.backtrack(grid, start_x, start_y)
                    break

        return ans


grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
grid2 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
print(Solution().uniquePathsIII(grid))
print(Solution().uniquePathsIII(grid2))
