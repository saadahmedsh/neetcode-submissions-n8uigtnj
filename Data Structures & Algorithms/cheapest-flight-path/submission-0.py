class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf") for i in range(n)]
        dist[src] = 0
        
        for i in range(k + 1):
            new_dist = dist[:]
            
            for u, v, w in flights:
                if dist[u] != float("inf") and dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist
        
        return dist[dst] if dist[dst] != float("inf") else -1