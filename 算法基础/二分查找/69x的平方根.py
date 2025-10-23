class Solution:
    # 牛顿迭代法
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        xn = x / 2
        xnext = (xn + x / xn) / 2
        while abs(xnext - xn) >= 1e-5:
            xn = xnext
            xnext = (xn + x / xn) / 2
        return int(xnext)
    # 二分法
    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right