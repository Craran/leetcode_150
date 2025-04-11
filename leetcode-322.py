from typing import List
from functools import cache
from math import inf

class Solution:
    # @staticmethod
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dfs(i, amount):
            if i < 0 and amount == 0:
                return 0
            if i < 0:
                return inf
            

            if amount < coins[i]:
                return dfs(i - 1, amount)
            
            return min(dfs(i - 1, amount), dfs(i, amount - coins[i]) + 1)



        res = dfs(n - 1, amount)
        if res == inf:
            return -1
        return res

# print(Solution.coinChange(None, [1, 2, 5], 11))