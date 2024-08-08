from typing import List
def removeDuplicates(nums: List[int]) -> int:
    p1 = p2 = 0
    while p2 < len(nums):
        while p2 < len(nums) and nums[p1] == nums[p2]:
            length = p2 - p1 + 1
            if length > 2:
                del nums[p2]
                p2 -= 1
            p2 += 1
        p1 = p2
        p2 += 1
    
    return p2 - 2

removeDuplicates([1,1,1,2,2,3])