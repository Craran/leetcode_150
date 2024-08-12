from typing import List, Dict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht: Dict[int, int] = {}
        for i, num in enumerate(nums):
            if num not in ht:
                ht[num] = i
            else:
                if abs(i - ht[num]) <= k:
                    return True
                else:
                    ht[num] = i


        return False