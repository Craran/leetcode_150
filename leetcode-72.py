class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        s = [[0 for _ in range(505)] for _ in range(505)]
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0:
                    s[i][j] = j
                if j == 0:
                    s[i][j] = i

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    s[i][j] = s[i - 1][j - 1]
                else:
                    s[i][j] = min(s[i - 1][j - 1], s[i - 1][j], s[i][j - 1]) + 1
        return s[l1][l2]