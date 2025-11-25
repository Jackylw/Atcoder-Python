from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []

        def backtrack(left, right):
            if left == n and right == n:
                ans.append("".join(path))
                return

            # 选择添加左括号
            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()

            # 选择添加右括号，左括号数量大于右括号数量时，才添加右括号
            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()

        backtrack(0, 0)
        return ans

print(Solution().generateParenthesis(3))