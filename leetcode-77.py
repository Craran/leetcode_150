from typing import List
from collections import deque

class Solution:
    @staticmethod
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = [False for _ in range(n + 5)]
        
        tmp = []
        ans = []
        
        def dfs(n: int, k: int, x: int, cnt: int) -> None:
            if cnt >= k:
                ans.append(tmp[:]) # 深浅拷贝问题！！！！
                return None
            
            for i in range(1, n + 1):
                if visited[i] == True or i < x:
                    continue
                
                visited[i] = True
                tmp.append(i)

                dfs(n, k, i, cnt + 1)

                visited[i] = False
                tmp.pop()
            return None

        dfs(n, k, 0, 0)

        return ans
            
                
"""
重点关注深浅拷贝问题：
https://chatgpt.com/c/d7bf37ab-2d28-4457-b0b8-f2eef1e02141
浅拷贝：
a = b
修改b也会修改a，因为只传递了引用

深拷贝：
a = copy.deepcopy(b)
修改b不会修改a，创建了b的副本

"""