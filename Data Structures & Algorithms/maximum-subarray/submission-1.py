class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]

        running_sum = 0
        res = float('-inf')

        for i in range(l):
            running_sum += nums[i]
            res = max(running_sum, res)

            if running_sum < 0:
                running_sum = 0
        
        
        
        return res