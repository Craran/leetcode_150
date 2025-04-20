from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        ans = 0
        while l < r:
            w = r - l
            s = min(height[l], height[r]) * w
            ans = max(ans, s)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return ans

