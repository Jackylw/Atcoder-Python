from typing import List


class Solution:
    # BFS_DFS
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])
        i, j = entrance
        queue = [(i, j, 0)]
        maze[i][j] = '+'
        while queue:
            i, j, step = queue.pop(0)
            for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= m < row and 0 <= n < col and maze[m][n] == '.':
                    # BFS_DFS 保证了第一次到达出口时，就是最近的出口
                    if m == 0 or m == row - 1 or n == 0 or n == col - 1:
                        return step + 1
                    maze[m][n] = '+'
                    queue.append((m, n, step + 1))
        return -1
