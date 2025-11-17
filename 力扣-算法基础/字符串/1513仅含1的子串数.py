class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        idx = 0
        while idx < len(s):
            lenth_one = 0
            while idx < len(s) and s[idx] == '1':
                idx += 1
                lenth_one += 1
            ans += lenth_one * (lenth_one + 1) // 2
        return ans % (10 ** 9 + 7)