N, M, C = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for i in range(0, N):
    tmp_c = C
    a = list(map(int, input().split()))
    for i in range(0, M):
        tmp_c += a[i] * B[i]
    if tmp_c > 0:
        count += 1
print(count)
