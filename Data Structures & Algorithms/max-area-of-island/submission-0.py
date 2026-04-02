class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
        q = collections.deque()
        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            q.append((r, c))
            current_area = 1

            while q:
                r, c = q.popleft()
                for n_row, n_col in directions:
                    r_new = r + n_row
                    c_new = c + n_col
                    if (0 <= r_new < rows) and (0 <= c_new < cols) and (r_new, c_new) not in visited and grid[r_new][c_new] == 1:
                        visited.add((r_new,c_new))
                        q.append((r_new, c_new))
                        current_area += 1
            return current_area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs(i, j))
                    

        return max_area
        