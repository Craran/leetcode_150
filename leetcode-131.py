from typing import List

class Solution:
    # @staticmethod
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        path = []

        def dfs(i):
            if i == n:
                # result.append(path)
                result.append(path.copy()) ### !!!path是引用类型，不copy会改变！
                return
            
            for j in range(i, n):
                sub = s[i: j + 1]
                if sub == sub[::-1]:
                    path.append(sub)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return result

# Solution.partition(None, "a")
        

        
