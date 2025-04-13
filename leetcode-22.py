from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        cnt = [0, 0]
        def dfs(i):
            if i > 2 * n:
                result.append(''.join(path))
                return
        
            if cnt[0] < n:
                cnt[0] += 1
                path.append('(')
                dfs(i + 1)
                cnt[0] -= 1
                path.pop()

            if cnt[1] < n and cnt[0] > cnt[1]:
                cnt[1] += 1
                path.append(')')
                dfs(i + 1)
                cnt[1] -= 1
                path.pop()

        dfs(1)
        return result
