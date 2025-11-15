a, b, c = map(str, input().split())
strs = a + b + c
new_str = "".join(sorted(strs, reverse=True))
print(int(new_str))
