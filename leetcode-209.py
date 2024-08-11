from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = nums[0]
        if sum >= target:
            return 1
        i = j = 0
        n = len(nums)
        result = 0x7f7f7f7f

        while j < n:
            while i < j and sum >= target:
                sum -= nums[i]
                i += 1
                
            while i <= j and sum < target and j < n:
                j += 1
                sum += nums[j]
            
            if sum >= target:
                result = min(result, j - i + i)

