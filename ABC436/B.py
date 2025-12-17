N = int(input())
grid = [[0] * N for _ in range(N)]
r, c = 0, (N - 1) // 2
k = 1
grid[r][c] = k
for _ in range(N * N - 1):
    r_up = (r - 1) % N
    c_right = (c + 1) % N
    if grid[r_up][c_right] == 0:
        r, c = r_up, c_right
    else:
        r_down = (r + 1) % N
        r, c = r_down, c

    k += 1
    grid[r][c] = k

for row in grid:
    print(' '.join(map(str, row)))
