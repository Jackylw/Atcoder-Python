S = input().strip()
n = len(S)

# [(char, count)]
segments = []
i = 0
while i < n:
    j = i
    while j < n and S[j] == S[i]:
        j += 1
    seg_len = j - i
    segments.append((S[i], seg_len))
    i = j

count = 0
for idx in range(len(segments) - 1):
    c1, len1 = segments[idx]
    c2, len2 = segments[idx + 1]

    if ord(c2) == ord(c1) + 1:
        # 贡献的子串数量 = 两段长度的最小值
        count += min(len1, len2)

print(count)