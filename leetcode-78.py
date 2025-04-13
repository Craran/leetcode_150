from typing import List

### 每个元素选或不选：https://www.bilibili.com/video/BV1mG4y1A7Gu?spm_id_from=333.788.videopod.sections&vd_source=e29812a3dd29c4766e522b717fe65124

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         result = []
#         path = []

#         def dfs(i):
#             if i == n:
#                 result.append(path.copy())

#             dfs(i + 1)

#             path.append(nums[i])
#             dfs(i + 1)
#             path.pop()

#         dfs(0)
#         return result

### 必须选，每个节点都是答案

## 当前操作：从j >= i 中选一个数
## 子问题：从 >= j的下标中构造子集
## 下一个子问题：从>= j + 1的下标中构造子集

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        path = []

        def dfs(i):
            result.append(path.copy())
            if i == n:
                return

            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return result



