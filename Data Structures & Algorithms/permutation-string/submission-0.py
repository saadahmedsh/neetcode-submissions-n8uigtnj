class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_map = {}
        curr_map = {}

        for i in range(len(s1)):
            freq_map[s1[i]] = 1 + freq_map.get(s1[i], 0)
            curr_map[s2[i]] = 1 + curr_map.get(s2[i], 0)

        if curr_map == freq_map:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            curr_map[s2[l]] -= 1
            if not curr_map[s2[l]]:
                del curr_map[s2[l]]
            l += 1
            curr_map[s2[r]] = 1 + curr_map.get(s2[r], 0)
            if curr_map == freq_map:
                return True

        return False   

        