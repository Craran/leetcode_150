from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda interval: interval[0])
        result: List[List[int]] = [intervals[0]]
        for interval in intervals[1:]:
            if result[-1][-1] >= interval[0]:
                result[-1][-1] = (interval[1] 
                                  if interval[1] > result[-1][-1] 
                                  else result[-1][-1])
            else:
                result.append(interval)
            
        return result