from typing import List

def majorityElement(self, nums: List[int]) -> int:
    h = {}
    for i in range(len(nums)):
        if nums[i] not in h.keys():
            h[nums[i]] = 1
            if h[nums[i]] > (len(nums) // 2):
                return nums[i]
        else:
            h[nums[i]] += 1
            if h[nums[i]] > (len(nums) // 2):
                return nums[i]
    return None