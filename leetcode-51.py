from typing import List

class Solution:
    # @staticmethod
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited_row = [False for _ in range(n + 5)]
        visited_col = [False for _ in range(n + 5)]
        visited_lefttop = [False for _ in range(2 * n - 1 + 5)]
        visited_righttop = [False for _ in range(2 * n - 1 + 5)]

        queens = [['.' for _ in range(n + 5)] for _ in range(n + 5)]
        result = []

        def dfs(x: int, y: int, cnt: int) -> None:
            if cnt >= n:
                # nonlocal result
                queens_slice = [row[1: n + 1] for row in queens[1: n + 1]]
                tmp = [''.join(row) for row in queens_slice]
                result.append(tmp)
                return None

            for i in range(x + 1, n + 1):
                # if visited_row[i] == True or visited_lefttop[i - j + n] == True \
                #       or visited_righttop[i + j] == True:
                #     continue
                for j in range(1, n + 1):
                    if visited_row[i] == True or visited_col[j] == True or \
                          visited_lefttop[i - j + n] == True or visited_righttop[i + j] == True:
                        continue
                    visited_row[i], visited_col[j] = True, True
                    visited_lefttop[i - j + n], visited_righttop[i + j] = True, True
                    queens[i][j] = 'Q'
                    dfs(i, j, cnt + 1)
                    visited_row[i], visited_col[j] = False, False
                    visited_lefttop[i - j + n], visited_righttop[i + j] = False, False
                    queens[i][j] = '.'
            return None
        
        dfs(0, 0, 0)

        return result

# Solution.totalNQueens(None, 4)
# Solution.solveNQueens(None, 4)