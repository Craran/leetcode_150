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
            while i <= j and sum >= target:
                length = j - i + 1
                if length == 1:
                    return 1
                result = min(result, length)
                sum -= nums[i]
                i += 1
            if j >= n - 1:
                break
            while sum < target and j < n - 1:
                j += 1
                sum += nums[j]
        
        return result if result != 0x7f7f7f7f else 0
            
            
                

