from typing import List
class Solution:
    def is_bool(self, string: List[int]) -> bool:
        if len(string) <= 1:
            return True
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - 1 - i]:
                return False
        return True
    def longestPalindrome(self, s: str) -> str:
        string: List[str] = []
        result: List[str] = []
        n = len(s)
        visited = [False for _ in range(len(s) + 5)]

        def dfs(x: int, n: int):
            if self.is_bool(string):
                result.append(string)
            for nx in range(x + 1, n):
                if visited[nx] == True:
                    continue
                visited[nx] = True
                string.append(s[nx])
                dfs(nx, n)
                visited[nx] = False
                string.pop()
            