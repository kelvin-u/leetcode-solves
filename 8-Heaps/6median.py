import heapq


class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num):
        heapq.heappush(self.smallHeap, -num)

        max = self.smallHeap[0]
        min = self.largeHeap[0]
        if self.smallHeap and self.largeHeap and -max > min:
            small_val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -small_val)

        # small heap is at least two elements larger than large heap
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            small_val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -small_val)

        if len(self.largeHeap) > len(self.smallHeap) + 1:
            large_val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -large_val)

    def findMedian(self):
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]

        return (-self.smallHeap[0] + self.largeHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(3)
# obj.addNum(2)
# obj.addNum(7)
# obj.addNum(4)
