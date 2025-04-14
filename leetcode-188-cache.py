from typing import List
from functools import cache
from math import inf

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, s, cnt):
            if cnt < 0:
                return -inf
            if i < 0 and s == 0:
                return 0
            if i < 0 and s == 1:
                return -inf

            if s == 1:
                return max(dfs(i-1, 1, cnt), dfs(i-1, 0, cnt-1) - prices[i])
            if s == 0:
                return max(dfs(i-1, 0, cnt), dfs(i-1, 1, cnt) + prices[i])

            
        return dfs(n-1, 0, k)
