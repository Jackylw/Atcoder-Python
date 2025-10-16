def f(n):
    s = 0
    if n == 0:
        return 1
    while n:
        s += n % 10
        n //= 10
    return s


n = int(input())
res = 0
for i in range(0, n):
    res += f(res)
print(res)
