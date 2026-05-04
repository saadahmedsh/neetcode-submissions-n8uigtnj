class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows , cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for i in range(rows)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]


        def dfs(i, j):

            if dp[i][j] != 0:
                return dp[i][j]


            max_len = 0

            for dx, dy in dirs:
                new_i = i + dx
                new_j = j + dy

                if 0 <= new_i < rows and 0 <= new_j < cols and matrix[new_i][new_j] > matrix[i][j]:
                    max_len = max(max_len, dfs(new_i, new_j))
                    

            dp[i][j] = 1 + max_len

            return dp[i][j]


        global_max = 0
        for i in range(rows):
            for j in range(cols):
                global_max = max(global_max, dfs(i, j))

        return global_max