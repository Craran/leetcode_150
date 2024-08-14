from typing import List
from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dr = [1, 0]
        dc = [0, 1]
        row = len(grid)
        col = len(grid[0])
        ans: List[List[int]] = [[0x3f3f3f3f for _ in range(col + 5)] for _ in range(row + 5)]
        visited: List[List[bool]] = [[False for _ in range(col + 5)] for _ in range(row + 5)]
        queue = deque()
        queue.append([0, 0])
        ans[0][0] = grid[0][0]

        def bfs() -> None:
            while queue:
                x, y = queue.popleft()
                for k in range(2):
                    nx, ny = x + dr[k], y + dc[k]
                    if nx > row - 1 or ny > col - 1:
                        continue
                    if visited[nx][ny] == True:
                        ans[nx][ny] = min(ans[nx][ny], ans[x][y] + grid[nx][ny])
                        
                    else:
                        visited[nx][ny] = True
                        ans[nx][ny] = ans[x][y] + grid[nx][ny]
                        queue.append([nx, ny])
        
        bfs()
        return ans[row - 1][col - 1]
