from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nr, nc = len(obstacleGrid), len(obstacleGrid[0])
        s = [[0 for _ in range(nc)] for _ in range(nr)]

        for i in range(nr):
            for j in range(nc):
                if i == 0 and j == 0:
                    s[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                elif i == 0:
                    s[i][j] = s[i][j - 1] if obstacleGrid[i][j] == 0 else 0
                elif j == 0:
                    s[i][j] = s[i - 1][j] if obstacleGrid[i][j] == 0 else 0
                else:
                    s[i][j] = s[i][j - 1] + s[i - 1][j] if obstacleGrid[i][j] == 0 else 0

        return s[nr - 1][nc - 1]   
