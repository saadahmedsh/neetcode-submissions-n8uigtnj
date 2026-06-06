from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        for s in stones:
            heappush(h, -s)

        while len(h) > 1:
            s1, s2 = -heappop(h), -heappop(h)
            if s1 > s2:
                heappush(h, -(s1 - s2))
            elif s2 > s1:
                heappush(h, -(s2 - s1))
            else:
                continue

        # print(s)
        return -h[-1] if h else 0 

        