from collections import deque

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

warp_map = {}
for r in range(H):
    for c in range(W):
        cell = grid[r][c]
        if cell.islower():
            if cell not in warp_map:
                warp_map[cell] = []
            warp_map[cell].append((r, c))

# BFS
queue = deque([(0, 0, 0)])  # 起点 (0,0)
visited = [[False] * W for _ in range(H)]
visited[0][0] = True

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上

while queue:
    r, c, steps = queue.popleft()

    if r == H - 1 and c == W - 1:
        print(steps)
        exit(0)

    cell = grid[r][c]
    if cell.islower():
        for nr, nc in warp_map[cell]:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.appendleft((nr, nc, steps))  # 0 步，所以放前面（0-1 BFS 优化）

    # 尝试行走
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and not visited[nr][nc]:
            visited[nr][nc] = True
            queue.append((nr, nc, steps + 1))

# 如果循环结束还没有找到路径，则输出 -1
print(-1)