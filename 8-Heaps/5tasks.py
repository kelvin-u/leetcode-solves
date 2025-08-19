from collections import deque
import heapq


class Solution:
    def leastInterval(self, tasks, n):
        # counter of all the elements
        count = {}

        for letter in tasks:
            count[letter] = count.get(letter, 0) + 1

        max_heap = [-values for values in count.values()]
        heapq.heapify(max_heap)

        q = deque()  # letter count, ready cycle
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                letter_count = heapq.heappop(max_heap) + 1
                if (
                    letter_count != 0
                ):  # if there exists some letter append it to the queue to go back into max heap
                    q.append(([letter_count, time + n]))

            print(q)
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time


tasks = ["A", "A", "A", "B", "B", "B"]
n = 3

sol1 = Solution()
print(sol1.leastInterval(tasks, n))
