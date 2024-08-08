from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    hash_table = {}
    cnt = 0
    result = []
    for i in range(len(nums)):
        if nums[i] not in hash_table:
            hash_table[nums[i]] = 1
            cnt += 1
        else:
            hash_table[nums[i]] += 1

    for key, val in hash_table.items():
        result.append(key)
    nums[:cnt] = result
    return cnt
