class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i, t in enumerate(temperatures):
            if not s or t < s[-1][1]:    
                s.append((i, t))
                continue
            while s and t > s[-1][1]:
                curr_i, curr_t = s.pop(-1)
                res[curr_i] = i - curr_i
            
            s.append((i, t))
        
        return res