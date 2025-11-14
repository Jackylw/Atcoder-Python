import heapq


class MedianFinder:

    def __init__(self):
        # max_heap 存储较小的一半元素（使用负数实现最大堆）
        self.max_heap = []
        # min_heap 存储较大的一半元素
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 维护两个堆的规则：
        # 1. max_heap的所有元素 <= min_heap的所有元素
        # 2. max_heap的大小 >= min_heap的大小，且相差不超过1
        
        # 第一步：决定将num添加到哪个堆
        # 如果num小于等于max_heap中最大的元素（即堆顶的相反数），则加入max_heap
        # 否则加入min_heap
        if self.max_heap and num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # 第二步：平衡两个堆的大小
        # 如果max_heap比min_heap多超过不止1个元素，将max_heap的堆顶移到min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            # 取出max_heap中最大的元素（需要恢复正数值）
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        # 如果min_heap比max_heap多，则将min_heap的堆顶移到max_heap
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        # 如果max_heap和min_heap大小相等，中位数是两个堆顶的平均值
        if len(self.max_heap) == len(self.min_heap):
            if not self.max_heap:  # 如果两个堆都为空
                return 0
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # 如果max_heap比min_heap多一个元素，中位数是max_heap的堆顶
        else:
            return -self.max_heap[0]


mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
