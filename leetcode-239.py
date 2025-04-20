from typing import List
from collections import deque


class Solution:
    # @staticmethod
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = deque()
        
        for i, x in enumerate(nums):
            while q and x > q[-1][1]:
                q.pop()

            q.append([i, x])
            if i - q[0][0] + 1 > k:
                q.popleft()
            ans.append(q[0][1])

        return ans[k-1:]
    
# Solution.maxSlidingWindow(None, [7,2,4], 2)
