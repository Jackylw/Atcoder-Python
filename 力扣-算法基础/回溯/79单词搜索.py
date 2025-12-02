from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 定义一个数组标记初始点位，即 word[0]
        rows = len(board)
        cols = len(board[0])
        mark = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # 找到 word[0]，开始查找
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    # word 从左往右一个一个匹配
                    if self.backtrack(i, j, mark, board, word[1:]):
                        return True
                    # 回溯
                    else:
                        mark[i][j] = 0
        return False

    def backtrack(self, i, j, mark, board, word):
        if not word:
            return True
        for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= m < len(board) and 0 <= n < len(board[0]) and board[m][n] == word[0]:
                if mark[m][n] == 1:
                    continue

                mark[m][n] = 1
                if self.backtrack(m, n, mark, board, word[1:]):
                    return True
                else:
                    mark[m][n] = 0
