from typing import List
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        row = len(forest)
        col = len(forest[0])
        tree = []
        for i in range(row):
            for j in range(col):
                if forest[i][j] > 1:
                    tree.append((forest[i][j], i, j))
        tree.sort()
        pre_i, pre_j = 0, 0
        ans = 0
        for _, i, j in tree:
            queue = deque([(0, pre_i, pre_j)])
            visited = set([(pre_i, pre_j)])  # 已访问坐标
            while queue:
                distance, x, y = queue.popleft()
                # 如果到达下一个树的位置
                if x == i and y == j:
                    ans += distance
                    pre_i, pre_j = i, j
                    break
                # 向四个方向移动
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    # 如果新位置在地图内，且未访问过，且不是障碍物
                    if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited and forest[nx][ny] > 0:
                        visited.add((nx, ny))
                        queue.append((distance + 1, nx, ny))
            else:
                return -1
        return ans
