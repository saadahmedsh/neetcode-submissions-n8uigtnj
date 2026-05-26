import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k

        for n in nums:
            if len(self.h) < k:
                heapq.heappush(self.h, n)
                continue
            if n > self.h[0]:
                _ = heapq.heappop(self.h)
                heapq.heappush(self.h, n)


        

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heapreplace(self.h, val)
        
        return self.h[0]



        
