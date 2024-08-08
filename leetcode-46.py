from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp = []
        visited = [False for _ in range(len(nums) + 5)]

        def dfs(x: int, cnt: int) -> None:
            if cnt >= len(nums):
                result.append(tmp[:])
                return None
            
            for i in range(len(nums)):
                if visited[i] == True:
                    continue
                visited[i] = True
                tmp.append(nums[i])
                dfs(i, cnt + 1)
                visited[i] = False
                tmp.pop()
            return None
        
        dfs(len(nums), 0)
        return result

            
"""
同样要注意深浅拷贝的问题
"""