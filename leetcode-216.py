from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        s = [0]
        def dfs(i):
            if len(path) == k:
                if sum(path) == n:
                    result.append(path.copy())
                return
            
            if k - len(path) > 9 - i + 1: # 剪枝：剩下的数不够到k个
                return
            
            if sum(path) + i > n:          # 剪枝：剩下的数最小的和大于n
                return
            

            for j in range(i, 10):
                if sum(path) + j <= n:
                    path.append(j)
                    dfs(j + 1)
                    path.pop()
            

        dfs(1)
        return result

                
