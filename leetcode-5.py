from typing import List

class Solution:
    # @staticmethod
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_length = 0
        result = ''
        for i in range(n):
            delta = 1
            # length = 1
            while True:
                if i - delta >= 0 and i + delta <= n - 1:
                    if s[i - delta] == s[i + delta]:
                        delta += 1
                        continue
                    length = 2 * (delta - 1) + 1
                    if length > max_length:
                        max_length = length
                        result = s[i - delta + 1: i + delta]
                        break
                    else:
                        break
                else:
                    length = 2 * (delta - 1) + 1
                    if length > max_length:
                        max_length = length
                        result = s[i - delta + 1: i + delta]
                        break
                    else:
                        break

        
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                continue
            delta = 1
            while True:
                if i - delta >= 0 and i + delta + 1 <= n - 1:
                    if s[i - delta] == s[i + 1 + delta]:
                        delta += 1
                        continue
                    length = 2 * (delta - 1) + 2
                    if length > max_length:
                        max_length = length
                        result = s[i - delta + 1: i + 1 + delta]
                        break
                    else:
                        break
                else:
                    length = 2 * (delta - 1) + 2
                    if length > max_length:
                        max_length = length
                        result = s[i - delta + 1: i + 1 + delta]
                        break
                    else:
                        break
        return result
    

# Solution.longestPalindrome(None, 'sss')
