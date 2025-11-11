class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        if n == 1:
            return ans
        # 添加外层循环来生成第n项
        for _ in range(n - 1):
            tmp = ""
            i = 0
            while i < len(ans):
                count = 1
                # 使用j变量来避免修改循环变量i
                j = i
                while j + 1 < len(ans) and ans[j] == ans[j + 1]:
                    count += 1
                    j += 1
                tmp += str(count) + ans[i]
                # 更新i到下一组不同字符的位置
                i = j + 1
            ans = tmp
        return ans

print(Solution().countAndSay(4))
print(Solution().countAndSay(1))
print(Solution().countAndSay(5))
