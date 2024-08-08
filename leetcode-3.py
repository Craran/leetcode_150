class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ht = {}
        result = 0
        for i in range(n):
            for j in range(i, n):
                if s[j] not in ht:
                    ht[s[j]] = True
                    result = max(result, j - i + 1)
                else:
                    ht.clear()
                    break
            
        return result
