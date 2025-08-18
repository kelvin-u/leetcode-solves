import heapq


class Solution:
    def lastStoneWeight(self, stones):
        max_heap = [-s for s in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)  # x = -8
            y = heapq.heappop(max_heap)  # y = -7

            if x != y:
                heapq.heappush(max_heap, x - y)

        return -max_heap[0] if max_heap else 0


stones = [2, 7, 4, 1, 8, 1]

stone1 = Solution()

print(stone1.lastStoneWeight(stones))
