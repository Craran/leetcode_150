from typing import List

def rob(self, nums: List[int]) -> int:
    n = len(nums)
    L = [0] * (n + 5)
    if n == 1:
        return nums[0]
        
    L[0], L[1] = nums[0], nums[1]
    for i in range(2, n):
        L[i] = max(L[i - 2], L[i - 3]) + nums[i]

    return max(L[n - 1], L[n - 2])
