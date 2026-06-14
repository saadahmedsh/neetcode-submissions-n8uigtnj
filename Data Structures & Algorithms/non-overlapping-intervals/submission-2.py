class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        prev = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            curr_start, curr_end  = interval
            if curr_start < prev:
                res += 1
                prev = min(curr_end, prev)
            else:
                prev = curr_end

        return res

        