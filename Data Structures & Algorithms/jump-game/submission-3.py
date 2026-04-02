class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        target = n - 1
        i = n - 2
        
        while  i >= 0:
            val = nums[i]
            diff = target - i
            if val >= diff:
                target = i
                i = i - 1
                continue
            if target == 0:
                return True
            i = i - 1
        
        return False if target != 0 else True

        


        