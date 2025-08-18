import heapq


class KthLargest:
    # nums is int[] nums
    # make a heap with k elements
    def __init__(self, k, nums):
        self.k = k
        self.minHeap = nums

        # remove elements until k length
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# [4, 5, 8]
obj1 = KthLargest(3, [2, 5, 4, 8])

print(obj1.minheap)
