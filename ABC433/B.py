n = int(input())
A = [int(i) for i in input().split()]
found = False
for i in range(n):
    found = False
    for j in range(i, -1, -1):
        if A[j] > A[i]:
            print(j + 1)
            found = True
            break
    if not found:
        print(-1)
