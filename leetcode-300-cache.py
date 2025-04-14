from typing import List
from functools import cache
from math import inf 

class Solution:
    # @staticmethod
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(inf)
        @cache
        def dfs(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            res = -1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j) + 1)

            # res = max(res, dfs(i - 1))
            if res == -1:
                return 1
            return res
        
        return dfs(n) - 1

# Solution.lengthOfLIS(None, [4,10,4,3,8,9])