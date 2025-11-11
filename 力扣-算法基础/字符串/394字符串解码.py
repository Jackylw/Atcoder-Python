class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        cur = ''
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((cur, num))
                cur = ''
                num = 0
            elif ch == ']':
                prev, k = stack.pop()
                cur = prev + cur * k
            else:
                cur += ch
        return cur

print(Solution.decodeString(Solution(), "3[a]2[bc]"))
print(Solution.decodeString(Solution(), "3[a2[c]]"))
print(Solution.decodeString(Solution(), "2[abc]3[cd]ef"))
print(Solution.decodeString(Solution(), "abc3[cd]xyz"))

        
