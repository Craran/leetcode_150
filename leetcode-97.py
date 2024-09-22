from typing import List

class Solution:
    # @staticmethod
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        f: List[List[bool]] = [[False for _ in range(205)] for _ in range(205)]
        f[0][0] = True
        for j in range(1, n2 + 1):
            f[0][j] = True if f[0][j - 1] == True and s2[j - 1] == s3[j - 1] else False
            if f[0][j] == False:
                break

        for i in range(1, n1 + 1):
            f[i][0] = True if f[i - 1][0] == True and s1[i - 1] == s3[i - 1] else False
            if f[i][0] == False:
                break

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                f[i][j] = True if f[i - 1][j] == True and s1[i - 1] == s3[i + j - 1] or \
                    f[i][j - 1] == True and s2[j - 1] == s3[i + j - 1] else False
                

        return f[n1][n2]

    

# Solution.isInterleave(None, "aabcc", "dbbca", "aadbbcbcac")

