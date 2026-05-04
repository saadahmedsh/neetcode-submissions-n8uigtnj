class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        
        n = len(str1)
        m = len(str2)
        
        
        dp = [[-1 for j in range(m)] for i in range(n)]
        
        def dfs(str1, str2, i, j, dp):
            if i == len(str1) or j == len(str2):
                return 0
                
            if dp[i][j] == -1:
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dfs(str1, str2, i + 1, j + 1, dp)
                else:
                    dp[i][j] = max(dfs(str1, str2, i + 1, j, dp), dfs(str1, str2, i, j + 1, dp))
                
            return dp[i][j]
        return dfs(str1, str2, 0, 0, dp)
        