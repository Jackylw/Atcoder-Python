class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            # 最后一个字母单独解码
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # 最后两个字母合并解码
            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
