from heapq import *
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)
        h = [-cnt for cnt in counts.values()]
        heapify(h)
        q = deque()

        time = 0

        while q or h:
            time += 1

            if h:
                freq = 1 + heappop(h)
                if freq != 0:
                    q.append((freq, time + n))

            if q and q[0][1] == time:
 
 
               heappush(h, q.popleft()[0])

        return time
     
        