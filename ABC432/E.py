N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = []
for i in range(Q):
    query.append(list(map(int, input().split())))


def solve1(A, x, y):
    A[x] = y


def solve2(A, l, r):
    pass


for i in range(len(query)):
    if query[i][0] == 1:
        solve1(A, query[i][1] - 1, query[i][2])
    else:
        solve2(A, query[i][1], query[i][2])
