class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = {i:[] for i in range(n)}

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        s = [0]

        while s:
            node = s.pop()
            if node in visited:
                continue
            visited.add(node)
            neighbours = adj[node]
            for nei in neighbours:
                s.append(nei)

        return len(visited)  == n

        