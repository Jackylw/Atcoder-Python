H, W = map(int, input().split())
if W % 2 == 0:
    print(H * (W // 2))
else:
    total = 0;
    if H % 2 == 0:
        total = H // 2 * (W // 2 + W // 2 + 1)
    else:
        total = (H // 2) * (W // 2 + W // 2 + 1) + (H // 2 + 1) * (W // 2)
    print(total)
