from typing import List

def removeElement(self, nums: List[int], val: int) -> int:
    cnt = 0
    result = []
    for i in range(len(nums)):
        if nums[i] != val:
            cnt += 1
            result.append(nums[i])
        else:
            pass
    nums[:cnt] = result
    return cnt

