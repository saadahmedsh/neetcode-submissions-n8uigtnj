from heapq import *

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        h = []
        res = [-1] * len(queries)

        q_sorted = [(q, i) for i, q in enumerate(queries)]
        q_sorted.sort(key = lambda x: x[0])

        intervals.sort(key = lambda x:x[0])

        j = 0
        for q, i in q_sorted:

            while j < len(intervals) and q >= intervals[j][0]:
                l, r = intervals[j]
                heappush(h, ((r - l) + 1, r))
                j += 1

            while h and h[0][1] < q:
                heappop(h)

            res[i] = h[0][0] if h else -1

        return res