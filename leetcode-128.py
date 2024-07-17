from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
    ht = {}
    result = 0

    for num in nums:
        if num not in ht:
            ht[num] = False

    for num in ht:
        if ht[num] == True:
            continue
        
        cnt = 1
        i = num
        ht[i] = True
        while True:
            if i + 1 in ht:
                cnt += 1
                ht[i + 1] = True
            else:
                break
            i += 1
        i = num
        while True:
            if i - 1 in ht:
                cnt += 1
                ht[i - 1] = True
            else:
                break
            i -= 1
        result = max(cnt, result)
    return result
            
        
    
