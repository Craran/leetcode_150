from typing import List
from collections import deque

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = set()
        tmp = []
        ans = []

        def dfs(n: int, k: int, x: int, cnt: int) -> None:
            if cnt >= k:
                tmp.append(k)
                ans.append(tmp)
                return
            
            for i in range(1, n + 1):
                if visited[i] != True and ...:
                    visited[i] = True
                    tmp.append(i)
                    dfs(n, k, i, cnt + 1)
                    tmp.pop()
                    visited[i] = False
                

            