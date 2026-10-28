class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        newInterval = intervals[0]
        res = []
        for start, end in intervals[1:]:
            if start <= newInterval[1]:
                newInterval[1] = max(newInterval[1], end)
            if newInterval[1] < start:
                res.append(newInterval)
                newInterval = [start, end]
        res.append(newInterval)
        return res
