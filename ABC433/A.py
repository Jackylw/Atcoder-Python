X, Y, Z = map(int, input().split())

if (X - Z * Y) % (Z - 1) == 0:
    t = (X - Z * Y) // (Z - 1)
    if t >= 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")