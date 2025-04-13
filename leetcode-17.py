from typing import List
from functools import cache


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        n = len(digits)
        if n == 0:
            return []
        result = {}
        s = []
        def dfs(i):
            if i + 1 > n - 1:
                res = ''.join(s)
                if res not in result:
                    result[res] = 1
                return
            for k, c in enumerate(m[int(digits[i + 1])]):
                s.append(c)
                dfs(i + 1)
                s.pop()

        dfs(-1)
        
        return list(result.keys())




                

            