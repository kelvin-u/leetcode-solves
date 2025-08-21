import heapq
from collections import deque


class MedianFinder:

    def __init__(self):
        self.smallHeap = []  # max_heap
        self.largeHeap = []  # min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)

        if self.smallHeap and self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            small_value = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -small_value)

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            small_value = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -small_value)

        if len(self.largeHeap) > len(self.smallHeap) + 1:
            large_val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -large_val)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        return (-self.smallHeap[0] + self.largeHeap[0]) / 2


# obj = MedianFinder()
# obj.addNum(3)
# obj.addNum(2)
# obj.addNum(7)
# obj.addNum(4)


def task(tasks, n):
    # make a freq count to max a max_heap
    count = {}

    for letter in tasks:
        count[letter] = count.get(letter, 0) + 1

    max_heap = [-value for value in count.values()]

    q = deque()  # pair -> remaining letter, cycle time
    time = 0

    while q or max_heap:
        time += 1

        if max_heap:
            remaining_letters = heapq.heappop(max_heap) + 1

            if remaining_letters != 0:
                q.append([remaining_letters, time + n])

        # once it's ready again

        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
    return time


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

print(task(tasks, n))
