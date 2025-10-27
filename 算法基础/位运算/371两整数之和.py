class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 标准位运算实现，避免超时
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)


