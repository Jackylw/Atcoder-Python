class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        stack = []
        num = 0
        operator = '+'  # 初始操作符设为'+'

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            
            # 当遇到操作符或到达字符串末尾时，处理前面的数字
            if s[i] in '+-*/' or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                elif operator == '/':
                    # int()函数来实现向零取整
                    stack.append(int(stack.pop() / num))
                
                operator = s[i]
                num = 0
        
        return sum(stack)

solution = Solution()
print(solution.calculate("3+2*2"))
print(solution.calculate(" 3/2 "))
print(solution.calculate(" 3+5 / 2 "))