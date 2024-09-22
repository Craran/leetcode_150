from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        f: List[List[int]] = [[0 for _ in range(c + 5)] for _ in range(r + 5)]
        result = 0

        for i in range(r):
            f[i][0] = 1 if matrix[i][0] == '1' else 0
            result = max(result, f[i][0])
        
        for j in range(c):
            f[0][j] = 1 if matrix[0][j] == '1' else 0
            result = max(result, f[0][j])

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == '0':
                    f[i][j] = 0

                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
                    result = max(result, f[i][j])

        return result * result

