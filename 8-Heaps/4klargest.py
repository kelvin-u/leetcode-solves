import heapq


class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2

sol1 = Solution()
print(sol1.findKthLargest(nums, k))
