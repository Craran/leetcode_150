from typing import List

class Solution:
    # @staticmethod
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = height[0]
        suffix[-1] = height[-1]
        ans = 0
        for i in range(1, n):
            prefix[i] = max(height[i], prefix[i - 1])

        for i in range(n - 2, -1, -1):
            suffix[i] = max(height[i], suffix[i + 1])

        for i in range(1, n - 1):
            rain = min(prefix[i-1], suffix[i+1]) - height[i]
            ans += max(rain, 0)

        return ans
    
# Solution.trap(None, [4,2,0,3,2,5])
    