from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    ns = {}
    for i, num in enumerate(nums):
        if num not in ns:
            ns[num] = []
            ns[num].append(i)
        else:
            ns[num].append(i)

    for i in range(len(nums)):
        if target - nums[i] in ns:
            if target - nums[i] == nums[i] and len(ns[nums[i]]) >= 2:
                return ns[nums[i]]
            elif target - nums[i] != nums[i]:
                ns[target - nums[i]].append(i)
                return ns[target - nums[i]]
            else:
                continue
        else:
            continue
            

# twoSum(None, [2,7,11,15], 9)