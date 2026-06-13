class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:          # overlap: merge
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:                                       # gap: start new interval
                res.append(intervals[i])

        return res