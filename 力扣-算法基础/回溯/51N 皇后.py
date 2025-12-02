from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化棋盘，用 '.' 表示空位
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def backtrack(row: int):
            # 如果已经放置完所有行，记录当前解
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for col in range(n):
                # 检查当前位置是否安全
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'  # 回溯

        def is_safe(row: int, col: int) -> bool:
            # 检查列
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # 检查左上对角线
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 检查右上对角线
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        backtrack(0)
        return res

print(Solution().solveNQueens(4))
