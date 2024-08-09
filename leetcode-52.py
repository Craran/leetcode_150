class Solution:
    # @staticmethod
    def totalNQueens(self, n: int) -> int:
        visited_row = [False for _ in range(n + 5)]
        visited_col = [False for _ in range(n + 5)]
        visited_lefttop = [False for _ in range(2 * n - 1 + 5)]
        visited_righttop = [False for _ in range(2 * n - 1 + 5)]

        result = 0
        def dfs(x: int, y: int, cnt: int) -> None:
            if cnt >= n:
                nonlocal result
                result += 1
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
                    dfs(i, j, cnt + 1)
                    visited_row[i], visited_col[j] = False, False
                    visited_lefttop[i - j + n], visited_righttop[i + j] = False, False
            return None
        
        dfs(0, 0, 0)

        return result

# Solution.totalNQueens(None, 4)
