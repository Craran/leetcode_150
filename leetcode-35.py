from typing import List
def searchInsert(self, nums: List[int], target: int) -> int:
    n = len(nums)
    if target <= nums[0]:
        return 0
    elif target > nums[n - 1]:
        return n
    
    l, r = 0, n - 1
    mid = 0 
    while l < r:
        mid = (l + r) // 2 + 1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid
        else:
            r = mid - 1

    return (l + r) // 2 + 1

print(searchInsert(None, [1,3,5,6], 4))