from typing import List
import collections


class Solution:
    # BFS_DFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curColor = image[sr][sc]
        if curColor == color:
            return image

        n, m = len(image), len(image[0])
        que = collections.deque([(sr, sc)])
        image[sr][sc] = color
        while que:
            x, y = que.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                # 连通并且颜色一致
                if 0 <= mx < n and 0 <= my < m and image[mx][my] == curColor:
                    image[mx][my] = color
                    que.append((mx, my))

        return image

    # DFS
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        currColor = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == currColor:
                image[x][y] = color
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m:
                        dfs(mx, my)

        if currColor != color:
            dfs(sr, sc)
        return image
