from typing import List


## 复杂度: 搜索树的叶子数 * 根到叶子的路径长度：O(k * C(n, k))
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def dfs(i):
            if len(path) == k:
                result.append(path.copy())

            if n - i + 1 < k - len(path):
                return
            
            for j in range(i, n + 1):
                path.append(j)
                dfs(j + 1)
                path.pop()


        dfs(1)
        return result
