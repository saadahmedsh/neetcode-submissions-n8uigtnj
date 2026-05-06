class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
    
        pac_visited = set()
        atlantic_visited = set()
        
        def dfs(r, c, visited):
            
            if (r,c) in visited:
                return
            
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
            
            
        for c in range(cols):
            dfs(0, c, pac_visited)
            dfs(rows - 1, c, atlantic_visited)
            
            
        for r in range(rows):
            dfs(r, 0, pac_visited)
            dfs(r, cols - 1, atlantic_visited)
            
            
        return [list(coord) for coord in pac_visited.intersection(atlantic_visited)]
        