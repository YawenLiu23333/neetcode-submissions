class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda interval:interval[0])
        res = []
        newInterval = intervals[0]
        
        for start, end in intervals[1:]:
            if start <= newInterval[1]:
                newInterval[1] = max(end,newInterval[1])
            else:
                res.append(newInterval)
                newInterval = [start, end]
        res.append(newInterval)
        return res




