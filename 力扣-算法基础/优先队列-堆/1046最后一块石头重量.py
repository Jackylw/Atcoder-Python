from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 创建大根堆，但是 Python 的 heapq 默认是小根堆，因此存储负数模拟大根堆，注意取元素的时候取反
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap) # 注：这里把列表原地转换为堆结构

        while len(max_heap) > 1:
            # 取最大俩值，大根堆性质 y >= x
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0