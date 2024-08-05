from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        result = 0

        while i < j:
            s = min(height[i], height[j]) * (j - i)
            result = max(s, result)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        return result