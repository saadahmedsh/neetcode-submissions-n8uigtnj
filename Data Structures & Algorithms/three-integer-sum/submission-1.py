class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i, n in enumerate(nums):
            
            if n > 0:
                break

            l, r = i + 1, len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while l < r:
                curr_sum = nums[l] + nums[r] + nums[i] 
                if curr_sum == 0:
                    
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1
                    
                    r -= 1
                    while r > i and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1



        return res