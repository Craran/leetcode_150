from typing import List
from functools import cache
from math import inf


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def dfs(i, j):
            if i + 1 == j:
                return 0
            
            if j == i + 2:
                return values[i] * values[j] * values[i+1]

            res = inf
            for k in range(i+1, j):
                
                res = min(res, dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])

            return res
        
        return dfs(0, n-1)
