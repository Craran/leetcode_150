from typing import List
from math import inf
from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, s):
            if i < 0 and s == 0:
                return 0
            if i < 0 and s == 1:
                return -inf
            if i < 0 and s == 2:
                return -inf
            
            if s == 0:
                return max(dfs(i - 1, 0), dfs(i - 1, 2))
            if s == 1:
                return max(dfs(i-1, 1), dfs(i-1, 0) - prices[i])
            if s == 2:
                return dfs(i-1, 1) + prices[i]
            
        return max(dfs(n-1, 0), dfs(n-1, 2))


