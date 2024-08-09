class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n - 1
        s = s.lower()
        while i < j:
            while ((s[i] < 'a' or s[i] > 'z') and (s[i] < '0' or s[i] > '9')) and i < j:
                i += 1
            while ((s[j] < 'a' or s[j] > 'z') and (s[j] < '0' or s[j] > '9')) and i < j:
                j -= 1
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
                