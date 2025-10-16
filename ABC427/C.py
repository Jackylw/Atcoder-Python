import sys

data = sys.stdin.read().strip().split()
if not data:
    exit(0)

n = int(data[0])
m = int(data[1])
edges = []
idx = 2
for i in range(m):
    u = int(data[idx]) - 1
    v = int(data[idx + 1]) - 1
    edges.append((u, v))
    idx += 2

ans = m
for s in range(1 << n):
    res = 0
    for u, v in edges:
        if ((s >> u) & 1) == ((s >> v) & 1):
            res += 1
    ans = min(ans, res)

print(ans)