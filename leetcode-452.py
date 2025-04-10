from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 1
        points.sort(key=lambda x: x[0])
        
        result: List[List[int]] = [points[0]]
        
        for i in range(1, n):
            if result[-1][1] >= points[i][0]:
                result[-1][0] = max(result[-1][0], points[i][0])
                result[-1][1] = min(result[-1][1], points[i][1])
            else:
                result.append(points[i])

        return len(result)
