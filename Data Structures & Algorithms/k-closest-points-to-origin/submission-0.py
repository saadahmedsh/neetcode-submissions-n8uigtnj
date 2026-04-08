import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(x, y):
                return -(x**2 + y**2)

        max_heap = []
        
        for x, y in points:
            dist = get_dist(x, y)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            elif dist > max_heap[0][0]:
                heapq.heapreplace(max_heap, (dist, x, y))
                
        return [[x, y] for d, x, y in max_heap]

        