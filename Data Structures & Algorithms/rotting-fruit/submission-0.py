class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])


        fresh = 0
        time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                else:
                    pass

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)

            for _ in range(length):
                r, c = q.popleft()

                for di, dj in directions:
                    x = r + di
                    y = c + dj

                    if x in range(rows) and y in range(cols) and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x, y))

            time += 1

        return time if fresh == 0 else -1
        