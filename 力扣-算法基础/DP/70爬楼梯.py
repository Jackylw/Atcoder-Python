class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        temp1 = 1
        temp2 = 2
        ans = 0
        for i in range(3, n + 1):
            ans = temp1 + temp2
            temp1 = temp2
            temp2 = ans

        return ans


print(Solution().climbStairs(2))
