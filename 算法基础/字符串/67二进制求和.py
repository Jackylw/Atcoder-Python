class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        return bin(num1 + num2)[2:]

    # 法二，模拟加法
    def addBinary2(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            total = digit_a + digit_b + carry
            res.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        return "".join(res[::-1])


print(Solution().addBinary("11", "1"))
print(Solution().addBinary("1010", "1011"))
