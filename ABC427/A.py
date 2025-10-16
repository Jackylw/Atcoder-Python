import sys

s = str(input())
mid_index = len(s) // 2
result = ""
for i in range(0, len(s)):
    if i != mid_index:
        result += s[i]
print(result)
