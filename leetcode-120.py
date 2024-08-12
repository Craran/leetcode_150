from typing import List
from collections import deque


class Solution:
    # @staticmethod
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nr, nc = len(triangle), len(triangle[len(triangle) - 1])
        dr, dc = 1, [0, 1]
        visited = [[False for _ in range(nc + 5)] for _ in range(nr + 5)]
        ans = [[0x3f3f3f3f for _ in range(nc + 5)] for _ in range(nr + 5)]
        
        queue = deque()
        queue.append([0, 0])
        ans[0][0] = triangle[0][0]

        def bfs() -> None:
            while queue:
                x, y = queue.popleft()
                for k in range(2):
                    nx, ny = x + dr, y + dc[k]
                    if (nx < 0 or nx > nr - 1) and (ny < 0 or ny > nx):
                        continue
                    queue.append([nx, ny])
                    ans[nx][ny] = min(ans[nx][ny], ans[x][y] + triangle[nx][ny])


        bfs()
        return min(ans[nr - 1])
    
# Solution.minimumTotal(None, [[2],[3,4],[6,5,7],[4,1,8,3]])

                    



