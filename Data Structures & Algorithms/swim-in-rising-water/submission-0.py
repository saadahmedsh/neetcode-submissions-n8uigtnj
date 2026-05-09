from heapq import *
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        h = [[grid[0][0], 0, 0]]
        max_height = 0
        visited = set()

        while h:
            val, row , col = heappop(h)
            max_height = max(val, max_height)

            if row == col == n-1:
                return max_height

            for new_row, new_col in ((row - 1, col), (row + 1, col),
                                 (row, col - 1), (row, col + 1)):
                if new_row in range(len(grid)) and new_col in range(len(grid[0])) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    heappush(h, [grid[new_row][new_col], new_row, new_col])

      
            


        