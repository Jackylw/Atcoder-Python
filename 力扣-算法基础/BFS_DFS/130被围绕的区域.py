from typing import List


class Solution:

    def bfs_T(self, board, i, j):
        row = len(board)
        col = len(board[0])
        queue = [(i, j)]
        board[i][j] = 'T'  # 标记为临时字符，表示已访问
        while queue:
            i, j = queue.pop(0)
            # 检查四个方向
            for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= m < row and 0 <= n < col and board[m][n] == 'O':
                    board[m][n] = 'T'  # 标记为临时字符
                    queue.append((m, n))

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        # 思路：从边界上的O开始，将所有与边界上的O相连的O标记为临时字符T，
        # 然后遍历整个棋盘，将剩余的O（被包围的）变为X，将临时标记T改回O

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i == 0 or i == row - 1 or j == 0 or j == col - 1):
                    self.bfs_T(board, i, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
