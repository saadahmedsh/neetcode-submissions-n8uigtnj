class Solution:

    def encode(self, strs: List[str]) -> str:

        res_str = ''
        for s in strs:
            curr_len = len(s)
            res_str += str(curr_len) + "#" + s

        return res_str

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []
        while i < len(s) - 1:
            start = i
            while s[i] != '#':
                i += 1
            l = int(s[start:i])
            res.append(s[i + 1: i + l + 1])
            i += l + 1 

        return res
