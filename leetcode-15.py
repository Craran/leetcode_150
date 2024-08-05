from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(0, len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            k = len(nums) - 1

            for j in range(i + 1, len(nums)):
                if j >= k:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while j < k:
                    if nums[k] + nums[j] + nums[i] < 0:
                        break
                    elif nums[k] + nums[j] + nums[i] == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        break
                    else:
                        k -= 1
                    
                        

        return result
                    
