def bitCount(num):
    count = 0
    while num > 0:
        if num & 1:
            count += 1
        num >>= 1
    return count


n = int(input())
a = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    for i in range(len(a)):
        a[i] = a[i] * bitCount(a[i])

print(*a)
