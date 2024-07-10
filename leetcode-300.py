from typing import List

# def lengthOfLIS(self, nums: List[int]) -> int:
    
#     n = len(nums)

#     memory = {} # 选中i的情况下，从i开始的最大序列长度
#     def L(nums: List[int], i: int) -> int:

#         if i >= n - 1:
#             memory[i] = 1
#             return 1

#         max_len = 1
        
#         for j in range(i + 1, n):
#             if nums[i] >= nums[j]:
#                 continue
#             elif j in memory.keys():
#                 max_len = max(max_len, memory[j] + 1)
#                 # memory[i] = max(memory[i], max_len)
#             else: # nums[i] < nums[j]
#                 max_len = max(max_len, L(nums, j) + 1)
#         memory[i] = max_len

#         return max_len
#     result = 1
#     for i in range(n):
#         result = max(L(nums, i), result)

#     return result
    
        
def lengthOfLIS(self, nums: List[int]) -> int:
    
    n = len(nums)
    L = [1] * n # **选中i的情况下**由i开始序列最长长度
    result = 1

    for i in reversed(range(n)):
        max_len = 1
        for j in range(i + 1, n):
            if nums[i] >= nums[j]:
                continue
            else: # nums[i] < nums[j]
               max_len = max(L[j] + 1, max_len)
        L[i] = max_len
        result = max(result, L[i])
    
    return result


    

