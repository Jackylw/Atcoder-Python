from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        # 最长公共前缀一定是两个字符串的公共前缀，所以先找到字典序最大和最小的字符串
        str1 = max(strs)
        str2 = min(strs)
        for i in range(len(str2)):
            if str1[i] != str2[i]:
                return ans
            ans += str1[i]
        return ans

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))