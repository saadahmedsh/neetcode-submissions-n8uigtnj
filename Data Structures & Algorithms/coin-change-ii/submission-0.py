class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}
        n = len(coins)


        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == n:
                return 0
            if (a,i) in cache.keys():
                return cache[(a,i)]

            cache[(a, i)] = dfs(i, a + coins[i]) + dfs(i + 1, a)

            return cache[(a, i)]

        return dfs(0,0)

        
        