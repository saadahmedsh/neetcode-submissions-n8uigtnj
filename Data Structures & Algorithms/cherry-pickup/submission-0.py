class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[None] * n for _1 in range(n)] for _2 in range(n)]
        
        
        def dfs(r1, c1, r2, c2):
            # r2 = c1 + c2 - r1
            if (r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
                
            if dp[r1][c1][c2] is not None:
                return dp[r1][c1][c2]
                
            if r1 == c1 == n-1:
                return grid[r1][c1]
                
            cherries = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
            total_cherries = cherries + max(
                dfs(r1 + 1, c1, r2 + 1, c2 ),
                dfs(r1 , c1 + 1, r2, c2 + 1 ),
                dfs(r1 + 1, c1, r2, c2 + 1),
                dfs(r1, c1 + 1, r2 + 1, c2)
                ) 
            dp[r1][c1][c2] = total_cherries
            
            return total_cherries
                
        return max(0, dfs(0,0,0,0))
        