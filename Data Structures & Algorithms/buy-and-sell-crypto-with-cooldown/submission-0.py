class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dfs(i, buy_or_not):

            if  i >= len(prices):
                return 0

            if (i, buy_or_not) in cache:
                return cache[(i, buy_or_not)]

            cooldown = dfs(i + 1, buy_or_not)
            if buy_or_not:
                cache[(i, buy_or_not)] = max(dfs(i + 1, False) - prices[i], cooldown)
            else:
                cache[(i, buy_or_not)] = max(dfs(i + 2, True) + prices[i], cooldown)

            return cache[(i, buy_or_not)]

        
        return dfs(0, True)