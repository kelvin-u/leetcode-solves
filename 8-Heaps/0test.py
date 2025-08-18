import heapq

list = [1, 3, 8, 3, 1, 2, 3, 6, 8, 5]

heapq.heapify(list)
print(list)

max_heap = []

for num in list:
    heapq.heappush(max_heap, -num)

print(max_heap)


while len(max_heap) > 2:
    if max_heap[0] == max_heap[1]:
        heapq.heappop(max_heap)
        heapq.heappop(max_heap)
    else:
        heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_heap[0] - max_heap[1])

print(max_heap)
