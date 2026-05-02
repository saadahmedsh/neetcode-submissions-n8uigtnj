class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far


        for i in range(1, len(nums)):
            prev_max_so_far = max_so_far
            max_so_far = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], prev_max_so_far * nums[i], min_so_far * nums[i])
            result = max(result,  max_so_far)



        return result