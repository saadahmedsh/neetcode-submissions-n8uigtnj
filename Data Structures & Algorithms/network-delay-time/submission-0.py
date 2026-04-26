from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        q = PriorityQueue()
        adj = {i + 1:[] for i in range(n)}
        
        for src, dst, time in times:
            adj[src].append((time, dst))
        
        visited = set()    
        q.put((0, k))
        max_delay = 0
        while not q.empty():
            time, node = q.get()
            if node in visited:
                continue
            
            max_delay = max(max_delay, time)
            neighbours = adj[node]
            visited.add(node)
            for time_nei, node_nei in neighbours:
                if node_nei in visited:
                    continue
                q.put((time_nei + time, node_nei))
                
        if len(visited) == n:
            return max_delay
            
        return -1
        