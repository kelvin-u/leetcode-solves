import heapq


class Solution:
    def kClosest(self, points, k):
        min_heap = []

        for x, y in points:
            d = x * x + y * y
            heapq.heappush(min_heap, (-d, [x, y]))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [item[1] for item in min_heap]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2

sol1 = Solution()
print(sol1.kClosest(points, 2))
