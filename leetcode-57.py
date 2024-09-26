from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        
        result: List[List[int]] = [[]]
        # flag = False
        r = l = -1
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[0]:
                l = i

            if newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]:
                r = i

        if l == -1 and r == -1:
            return [newInterval]
        elif l == -1:
            newInterval[1] = max(newInterval[1], intervals[r][1])
            return [newInterval] + intervals[r + 1: ] if r < len(intervals) - 1 else [newInterval]
        elif r == -1:
            newInterval[0] = min(newInterval[0], intervals[l][0])
            return [newInterval] if l == 0 else intervals[: l] + [newInterval]
        else:
            newInterval[1] = max(newInterval[1], intervals[r][1])
            newInterval[0] = min(newInterval[0], intervals[l][0])
            return intervals[: l] + [newInterval] + intervals[r + 1: ]


