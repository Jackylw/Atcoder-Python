from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        s_list = list(s)

        def backtrack(cur_s, index):
            if index == len(cur_s):
                ans.append("".join(cur_s))
                return

            if cur_s[index].isalpha():
                # 要么转为小写
                s_list[index] = s_list[index].lower()
                backtrack(s_list, index + 1)

                # 要么转为大写
                s_list[index] = s_list[index].upper()
                backtrack(s_list, index + 1)
            else:
                # 纯数字，跳过
                backtrack(s_list, index + 1)

        backtrack(s_list, 0)
        return ans


print(Solution().letterCasePermutation("a1b2"))
print(Solution().letterCasePermutation("3z4"))
