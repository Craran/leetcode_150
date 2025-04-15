from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i, j):
            if i == j:
                return 1
            if i + 1 == j:
                if s[i] == s[j]:
                    return 2
                
            if s[i] == s[j]:
                return dfs(i+1, j-1) + 2
            return max(dfs(i+1, j), dfs(i, j-1))
        



        return dfs(0, n-1)
