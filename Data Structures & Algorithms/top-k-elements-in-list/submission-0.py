from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}


        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        h = []

        for key, val in freq.items():
            heappush(h, (-val, key))

        res = []
        for i in range(k):
            f, val = heappop(h)
            res.append(val)

        return res              