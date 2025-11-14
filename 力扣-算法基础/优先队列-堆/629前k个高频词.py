from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = Counter(words)
        heap = []
        for word, freq in freq_map.items():
            heapq.heappush(heap, (-freq, word))
        res = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            res.append(word)
        return res


print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
