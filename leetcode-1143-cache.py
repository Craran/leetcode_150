from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            
            
            if text1[i] == text2[j]:
                res = dfs(i - 1, j - 1) + 1
            else:
                res = max(dfs(i - 1, j), dfs(i, j - 1))
            return res
        
        
        return dfs(n1 - 1, n2 - 1)