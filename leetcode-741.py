from typing import List
from collections import deque
from math import inf

class Solution:
    # @staticmethod
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # s = [[0 for _ in range(n + 5)] for _ in range(n + 5)]
        # s[0][0] = grid[0][0]
        # for y in range(1, n):
        #     if grid[0][y] == -1 or s[0][y - 1] == -1:
        #         s[0][y] = -1
        #         continue
        #     s[0][y] = s[0][y - 1] + grid[0][y]

        # for x in range(1, n):
        #     if grid[x][0] == -1 or s[x - 1][0] == -1:
        #         s[x][0] = -1
        #         continue
        #     s[x][0] = s[x - 1][0] + grid[x][0]
        
        # for x in range(1, n):
        #     for y in range(1, n):
        #         if grid[x][y] == -1:
        #             s[x][y] = -1
        #             continue
        #         # if grid[x - 1][y] == -1 and grid[x][y - 1] == -1:
        #         #     s[x][y] = -1
        #         #     continue
        #         if s[x - 1][y] == -1 and s[x][y - 1] == -1:
        #             s[x][y] = -1
        #             continue
        #         s[x][y] = max(s[x - 1][y], s[x][y - 1]) + grid[x][y]

        # if s[n - 1][n - 1] == -1:
        #     return 0

        dp = [[[-inf] * (n + 5) for _ in range(n + 5)] for _ in range(2 * n + 5)]
        dp[0][0][0] = grid[0][0]

        for step in range(1, 2 * n - 1):
            for x1 in range(n):
                y1 = step - x1
                if y1 < 0 or y1 > n - 1 or grid[x1][y1] == -1:
                    continue
                for x2 in range(n):
                    y2 = step - x2
                    if y2 < 0 or y2 > n - 1 or grid[x2][y2] == -1:
                        continue
                    dp[step][x1][x2] = max(dp[step - 1][x1][x2], dp[step][x1][x2])
                    if x1 != 0:
                        dp[step][x1][x2] = max(dp[step - 1][x1 - 1][x2], dp[step][x1][x2])
                    if x2 != 0:
                        dp[step][x1][x2] = max(dp[step - 1][x1][x2 - 1], dp[step][x1][x2])
                    if x1 != 0 and x2 != 0:
                        dp[step][x1][x2] = max(dp[step - 1][x1 - 1][x2 - 1], dp[step][x1][x2])
                    dp[step][x1][x2] += grid[x1][y1]
                    if x1 != x2:
                        dp[step][x1][x2] += grid[x2][y2]

        return max(0, dp[2 * n - 2][n - 1][n - 1])
    

                    
