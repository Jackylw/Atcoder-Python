from typing import List
from typing import Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 使用集合记录每行、列、宫格中已有的数字
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # 初始化已有数字
        empty_cells = []  # 存放空位置，后续仅遍历这些位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)  # 第几个宫
                else:
                    empty_cells.append((i, j))

        def backtrack(idx: int) -> bool:
            if idx == len(empty_cells):
                return True

            i, j = empty_cells[idx]
            box_idx = (i // 3) * 3 + j // 3

            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
                    # 做选择
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(idx + 1):
                        return True

                    # 撤销选择
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_idx].remove(num)

            return False

        backtrack(0)

    # 启发式算法
    def solveSudoku2(self, board: List[List[str]]) -> None:
        # 约束记录
        rows = [set(str(i) for i in range(1, 10)) for _ in range(9)]  # 每行剩余可用数字
        cols = [set(str(i) for i in range(1, 10)) for _ in range(9)]
        boxes = [set(str(i) for i in range(1, 10)) for _ in range(9)]

        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].discard(num)
                    cols[j].discard(num)
                    boxes[(i // 3) * 3 + j // 3].discard(num)
                else:
                    empty_cells.append((i, j))

        # 使用 set 存储空格坐标，便于动态删除/恢复
        empty_set = set(empty_cells)

        def get_candidates(i: int, j: int) -> Set[str]:
            """返回 (i,j) 当前可选数字"""
            box_idx = (i // 3) * 3 + j // 3
            return rows[i] & cols[j] & boxes[box_idx]

        def backtrack() -> bool:
            if not empty_set:
                return True

            # MRV: 找到可选数字最少的空格
            best_cell = None
            min_options = 10
            best_candidates = None

            for (i, j) in empty_set:
                candidates = get_candidates(i, j)
                if not candidates:  # 无解
                    return False
                if len(candidates) < min_options:
                    min_options = len(candidates)
                    best_cell = (i, j)
                    best_candidates = candidates
                    if min_options == 1:  # 最优情况，无需继续找
                        break

            i, j = best_cell
            box_idx = (i // 3) * 3 + j // 3
            empty_set.remove((i, j))

            for num in best_candidates:
                # 做选择
                board[i][j] = num
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[box_idx].remove(num)

                if backtrack():
                    return True

                # 撤销选择
                board[i][j] = '.'
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)

            empty_set.add((i, j))
            return False

        backtrack()


board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "9", ".", ".", "1", ".", ".", "3", "."],
         [".", ".", "6", ".", "2", ".", "7", ".", "."],
         [".", ".", ".", "3", ".", "4", ".", ".", "."],
         ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", "2", "5", ".", "6", "4", ".", "."],
         [".", "8", ".", ".", ".", ".", ".", "1", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]

Solution().solveSudoku2(board)
print(board)
