class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        n = len(sx)
        for i in range(n // 2):
            if sx[i] != sx[n - 1 - i]:
                return False

        return True