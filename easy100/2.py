# https://atcoder.jp/contests/abc156/tasks/abc156_c

N = int(input())
X = list(map(int, input().split()))
sums = []
for p in range(0, max(X) + 1):
    s = 0
    for i in range(0, N):
        s += (X[i] - p) ** 2
    sums.append(s)
print(min(sums))
