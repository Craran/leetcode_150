from typing import List
from collections import deque

# class Solution:
#     # @staticmethod
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         dr, dc = 1, [0, 1]
#         cost = [[int(1e9+5) for _ in range(i)] for i in range(1, len(triangle) + 1)]
#         n = len(triangle)

#         queue = deque()
#         queue.appendleft([0, 0])
#         cost[0][0] = triangle[0][0]

#         while queue:
#             x, y = queue.pop()
#             for i in range(2):
#                 nx, ny = x + dr, y + dc[i]
#                 if nx >= 0 and nx <= n - 1:
#                     cost[nx][ny] = min(cost[nx][ny], cost[x][y] + triangle[nx][ny])
#                     queue.appendleft([nx, ny])

#                 else:
#                     continue
        
#         return min(cost[n - 1])


class Solution:
    # @staticmethod
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        ans = [[0x3f3f3f3f for j in range(n)] for i in range(n)]
