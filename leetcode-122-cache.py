from typing import List
from functools import cache
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, s):
            if i < 0 and s == 0:
                return 0
            if i < 0 and s != 0:
                return -inf
            if s == 0:
                return max(dfs(i - 1, 0), dfs(i - 1, 1) + prices[i])
            return max(dfs(i - 1, 1), dfs(i - 1, 0) - prices[i])
        
        return dfs(n - 1, 0)