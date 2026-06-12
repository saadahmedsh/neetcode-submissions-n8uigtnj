class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = l + ((r - l) // 2)
                if nums[m] == target:
                    return True
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return False
        
        u = 0
        d = len(matrix) - 1

        while u <= d:
            m = u + ((d - u) // 2)
            if matrix[m][0] == target or binary_search(matrix[m]):
                return True
            if matrix[m][0] < target:
                u = m + 1
            else:
                d = m - 1

        return False
            
            