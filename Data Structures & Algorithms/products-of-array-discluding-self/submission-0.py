class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

                
        prod = 1
        zero_count = 0
        zero_index = 0
        
        for i, n in enumerate(nums):
            if n != 0:
                prod *= n
            else:
                zero_count += 1
                zero_index = i
                
        if zero_count > 1:
            return [0] * len(nums)
            
        if zero_count == 1:
            res = [0] * len(nums)
            res[zero_index] = prod
            return res
                
        res = []
        
        for n in nums:
            if n == 0:
                continue
            res.append(prod // n)
        return res
        