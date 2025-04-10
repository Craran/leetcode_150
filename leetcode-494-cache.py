from typing import List
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        p2 = s + target
        if p2 < 0 or p2 % 2 != 0:
            return 0
        p = p2 // 2
        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        

        result = dfs(n - 1, p)
        return result