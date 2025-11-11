from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # 统计 t 中各字符出现次数
        t_counter = Counter(t)
        # 滔动窗口中各字符出现次数
        window_counter = Counter()

        # 滑动窗口的左右指针
        left = 0
        right = 0

        # 记录最小窗口的信息
        min_len = float('inf')
        min_start = 0

        # 记录已满足条件的字符种类数
        formed = 0
        required = len(t_counter)

        while right < len(s):
            # 扩大窗口
            char = s[right]
            window_counter[char] += 1

            # 如果当前字符的频次满足要求，增加 formed 计数
            if char in t_counter and window_counter[char] == t_counter[char]:
                formed += 1

            # 尝试收缩窗口
            while left <= right and formed == required:
                char = s[left]

                # 更新最小窗口
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # 收缩窗口
                window_counter[char] -= 1
                if char in t_counter and window_counter[char] < t_counter[char]:
                    formed -= 1

                left += 1

            right += 1

        # 返回最小覆盖子串
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]


# 测试
s1 = Solution().minWindow("ADOBECODEBANC", "ABC")
print(s1)
