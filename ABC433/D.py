from collections import defaultdict

N, M = map(int, input().split())
A = [int(x) for x in input().split()]
groups = [defaultdict(int) for _ in range(11)]  # 索引0不用，1~10

for x in A:
    L = len(str(x))
    groups[L][x % M] += 1

count = 0

# 预计算 10^L mod M 对于 L=1 到 10
pow10_mod = [0] * 11
for L in range(1, 11):
    pow10_mod[L] = pow(10, L, M)

# 枚举每个 A[i] 作为左半部分
for i in range(N):
    a = A[i]
    a_mod = a % M

    # 尝试所有可能的右半部分长度 L (1 到 10)
    for L in range(1, 11):
        if not groups[L]:  # 该长度没有数字，跳过
            continue

        power_val = pow10_mod[L]
        # 我们需要: (a * 10^L + b) ≡ 0 (mod M)
        # => b ≡ (-a * 10^L) mod M
        target = (-a_mod * power_val) % M

        # 累加该长度下余数为 target 的数字个数
        count += groups[L].get(target, 0)

print(count)