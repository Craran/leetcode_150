from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        j = n - 1

        for i in range(n):
            rest = target - numbers[i]
            while rest < numbers[j] and j > i:
                j -= 1
            if i >= j :
                break
            if rest == numbers[j]:
                return [i + 1, j + 1]
            else:
                continue



        return None

