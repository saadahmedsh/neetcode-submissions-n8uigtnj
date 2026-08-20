class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
       
        n = len(matchsticks)
        sticks_sum = sum(matchsticks)
        side_length = sticks_sum // 4
        if sticks_sum  % 4 != 0:
            return False
        
        

        
        lengths = [0,0,0,0]
        
        matchsticks.sort(reverse = True)
        # 2, 2, 2, 1, 1
        def backtrack(i):
            if i == n:
                return True
                
            for j in range(4):
                if lengths[j] + matchsticks[i] <= side_length:
                    lengths[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    lengths[j] -= matchsticks[i]
                    
            return False
        return backtrack(0)
        