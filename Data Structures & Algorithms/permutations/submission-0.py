class Solution:
    def permute(self, word: List[int]) -> List[List[int]]:
      
        result = []
        
        if len(word) == 0:
            return [[]]
            
        perms = self.permute(word[1:])
        for i in range(len(perms)):
            
            for j in range(len(perms[i]) + 1):
                p_copy = perms[i].copy()
                p_copy.insert(j, word[0])
                result.append(p_copy)
                
        return result