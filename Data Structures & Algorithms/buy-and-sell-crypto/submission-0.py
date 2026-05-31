class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        left_min = prices[0]

        for n in prices:
            if n < left_min:
                left_min = n
                continue

            res = max(res, n - left_min)
            left_min = min(left_min, n)

        return res
            
            
        