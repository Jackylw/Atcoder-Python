from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        # 单词长度和单词数量
        word_len = len(words[0])
        word_count = len(words)
        s_len = len(s)

        # 统计目标单词出现次数
        target_counter = Counter(words)
        result = []

        # 多起点滑动窗口：从0到word_len-1的每个位置开始
        for start in range(word_len):
            left = start
            window_counter = defaultdict(int)
            matched_count = 0

            # 以单词为单位滑动窗口
            for right in range(start, s_len - word_len + 1, word_len):
                # 获取当前单词
                current_word = s[right:right + word_len]

                # 如果是目标单词
                if current_word in target_counter:
                    window_counter[current_word] += 1
                    matched_count += 1

                    # 如果当前单词数量超过需求，收缩窗口左侧
                    while window_counter[current_word] > target_counter[current_word]:
                        left_word = s[left:left + word_len]
                        window_counter[left_word] -= 1
                        matched_count -= 1
                        left += word_len

                    # 如果完全匹配所有单词，记录结果
                    if matched_count == word_count:
                        result.append(left)
                else:
                    # 遇到无关单词，重置窗口
                    window_counter.clear()
                    matched_count = 0
                    left = right + word_len

        return result
