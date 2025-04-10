from typing import List
from functools import cache, lru_cache, cached_property

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * (n + 5)
        # @lru_cache
        def dfs(i):
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
                
            result = max(dfs(i - 1), dfs(i - 2) + nums[i])
            cache[i] = result
            return result
        
        return dfs(n - 1)
        
