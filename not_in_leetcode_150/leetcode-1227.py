from typing import List

class Solution:
    # @staticmethod
    def countSquares(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        f: List[List[int]] = [[0 for _ in range(c + 5)] for _ in range(r + 5)]

        cnt = 0
        
        for i in range(r):
            f[i][0] = 1 if matrix[i][0] == 1 else 0

        for j in range(c):
            f[0][j] = 1 if matrix[0][j] == 1 else 0

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
        
        for i in range(r):
            for j in range(c):
                cnt += f[i][j]

        return cnt
    

# Solution.countSquares(None, [[0,1,1,1],[1,1,1,1],[0,1,1,1]])