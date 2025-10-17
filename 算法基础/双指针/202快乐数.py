class Solution:
    def f(self, n):
        total = 0
        while n > 0:
            total += (n % 10) ** 2
            n = n // 10
        return total
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.f(n)
        while slow != fast:
            slow = self.f(slow)
            fast = self.f(self.f(fast))
        return slow == 1