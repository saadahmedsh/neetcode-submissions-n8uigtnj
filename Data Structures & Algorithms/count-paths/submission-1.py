class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bottom_row = [1] * n

        for i in range(m - 2, -1, -1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + bottom_row[j]
            bottom_row = new_row

        return bottom_row[0]
        
        