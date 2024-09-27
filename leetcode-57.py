from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        
        
        l = r = -1
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][1]:
                l = i
                break

        for i in reversed(range(len(intervals))):
            if newInterval[1] >= intervals[i][0]:
                r = i
                break

        if l == -1:
            return intervals + [newInterval]
        elif r == -1:
            return [newInterval] + intervals
        else:
            newInterval[0] = min(newInterval[0], intervals[l][0])
            newInterval[1] = max(newInterval[1], intervals[r][1])
            return intervals[0: l] + [newInterval] + intervals[r + 1: ]
            

