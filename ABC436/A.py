N = int(input())
S = input()
s_len = len(S)
if N < s_len:
    ans = S
else:
    s_o = 'o' * (N - s_len)
    ans = s_o + S

print(ans)
