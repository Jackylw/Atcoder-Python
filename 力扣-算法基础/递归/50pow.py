class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n # 现在 n 为正数

        res = 1.0
        base = x

        while n:
            if n & 1: #如果 n 是奇数
                res *= base
            base *= base
            n >>= 1
        return res

print(Solution().myPow(2.00000, 10))
        
