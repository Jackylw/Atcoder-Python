class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_count = 0
        while right < len(s):
            if s[right] not in s[left:right]:
                max_count = max(max_count, right - left + 1)
                right += 1
            else:
                left += 1
        return max_count

s1 = Solution().lengthOfLongestSubstring('abcabcbb')
print(s1)
s2 = Solution().lengthOfLongestSubstring('bbbbb')
print(s2)
s3 = Solution().lengthOfLongestSubstring('pwwkew')
print(s3)