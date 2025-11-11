class Solution:
    def modifyString(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] == "?":
                for j in "abc":
                    if i - 1 >= 0 and s[i - 1] == j:
                        continue
                    if i + 1 < len(s) and s[i + 1] == j:
                        continue
                    s = s[:i] + j + s[i + 1:]
                    break
        return s