from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 5)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][0] + nums[i], dp[i][0])

        return max(dp[n - 1][0], dp[n - 1][1])