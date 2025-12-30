n = 20240601
dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 7
for i in range(3, n + 1):
    dp[i] = dp[i-1] + 3 * i + 2 * (i - 2)
print(dp[n])
