import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # The kth largest element is at index (len(nums) - k) 
        # in a sorted version of the array.
        target_idx = len(nums) - k

        def quick_select(l, r):
            # 1. Random Pivot Selection (Crucial for performance)
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            
            pivot, p = nums[r], l

            # 2. Partitioning (Lomuto Scheme)
            for i in range(l, r):                
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            # Move pivot to its final sorted position
            nums[r], nums[p] = nums[p], nums[r]

            # 3. Binary Search-like Selection
            if target_idx == p:
                return nums[p]
            elif target_idx > p:
                return quick_select(p + 1, r)
            else:
                return quick_select(l, p - 1)

        return quick_select(0, len(nums) - 1)