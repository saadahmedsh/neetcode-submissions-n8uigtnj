import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
        q = collections.deque()
        num_islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                for n_row, n_col in directions:
                    r_new = r + n_row
                    c_new = c + n_col
                    if (0 <= r_new < rows) and (0 <= c_new < cols) and (r_new, c_new) not in visited and grid[r_new][c_new] == "1":
                        visited.add((r_new,c_new))
                        q.append((r_new, c_new))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    num_islands += 1

        return num_islands