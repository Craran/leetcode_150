from typing import List
from collections import deque




# def lengthOfLIS(self, nums: List[int]) -> int:
#     n = len(nums)
#     visited = set()

#     stack = deque()
#     L = {}
#     L[n - 1] = 1

#     for i in range(n):
#         stack.append(i)
    
#     while len(stack) > 0:

#         top = stack.pop()

#         for i in range(top + 1, n):
#             if nums[i] <= nums[top]:
#                 pass
#             else:
#                 stack.append(i)
#                 if i in L:
#                     L[top] = max(L[top], L[i] + 1)
#                     continue
#                 else:
                    


def lengthOfLIS(self, nums: List[int]) -> int:

    # memory = {}
    def L(nums=nums, i=0) -> int:
        if i == len(nums) - 1:
            return 1
        else:
            pass

        max_len = 1
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                max_len = max(max_len, L(nums, j) + 1)
            else:
                pass
    
    return
