from typing import List


class Solution:
    # 排序对比法，时间复杂度高
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_sort = sorted(p)
        windows = len(p)
        ans = []
        for i in range(len(s) - windows + 1):
            if sorted(s[i:i + windows]) == p_sort:
                ans.append(i)
        return ans

    # 滑动窗口优化
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        # 统计 p 中字符出现的次数
        p_count = {c: p.count(c) for c in p}
        # 初始化窗口字符频次统计
        window_count = {}

        ans = []
        window_len = len(p)

        for i in range(len(s)):
            # 进窗口
            window_count[s[i]] = window_count.get(s[i], 0) + 1

            # 窗口超过 p 长度，移除左边字符
            if i >= window_len:
                left_char = s[i - window_len]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]

            # 判断窗口字符频次是否与 p 中字符频次相同
            if window_count == p_count:
                ans.append(i - window_len + 1)

        return ans