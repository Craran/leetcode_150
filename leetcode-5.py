from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = 0
        state = [1 for _ in range(n + 5)]
        for i in range(n):
            if i == 1 or i == n - 1:
                state[i] = 1
                continue
            j = i + 1
            while (j - i) + i <= n - 1 and i - (j - i) >= 0:
                if s[j] == s[i - (j - i)]:
                    state[i] = max()