class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2  = len(word1), len(word2)
        s = [[0 for _ in range(n2 + 5)] for _ in range(n1 + 5)]
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 and j == 0:
                    s[i][j] = 0
                elif i == 0:
                    s[i][j] = j
                elif j == 0:
                    s[i][j] = i
                else:
                    s[i][j] = min(s[i - 1][j - 1] 
                                  if word1[i - 1] == word2[j - 1]
                                  else s[i - 1][j - 1] + 1,
                                  s[i][j - 1] + 1,
                                  s[i - 1][j] + 1)
        return s[n1][n2]
            
                    
