from math import log2


def h(total_0) -> bool:
    n = 23333333
    total_1 = n - total_0
    if total_0 == 0 or total_1 == 0:
        H_s = 0
    else:
        p0 = total_0 / n
        p1 = total_1 / n
        H_s = -total_0 * p0 * log2(p0) - total_1 * p1 * log2(p1)

    if abs(H_s - 11625907.5798) < 1e-4:
        return True
    return False


n = 23333333
for i in range(1, n // 2 + 1):  # 在较小范围内搜索
    if h(i):
        print(i)
        break
