from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        # 构造小根堆，假设小根堆只有 K 个元素，那么第 K 大的元素就是堆顶元素
        # 因此我们保证小根堆恰好只有 K 个元素即可
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
