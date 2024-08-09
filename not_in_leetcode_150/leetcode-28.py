class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + '#' + haystack
        n = len(s)
        pi = [0 for _ in range(n + 5)]
        for i in range(1, n):
            length = pi[i - 1]
            while length > 0 and s[length] != s[i]:
                length = pi[length - 1]
            if s[length] == s[i]:
                pi[i] = length + 1
            
        for i in range(n):
            if pi[i] == len(needle):
                return i - 2 * len(needle) 
            
        return -1

