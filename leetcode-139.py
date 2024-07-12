from typing import List

# 记忆化搜索
# def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#     n = len(s)
#     words = {}
#     positions = {}
#     result = {}
#     for word in wordDict:
#         if word not in words:
#             words[word] = len(word)
    
#     for i in range(n):
#         if s[:i + 1] in words:
#             positions[i] = True
#             result[i] = True

#     def dfs(position: int) -> None:
#         for i in range(position + 1, n):
#             if i in result:
#                 continue

#             if s[position + 1: i + 1] in words:
#                 result[i] = True
#                 dfs(i)
#             else:
                
#                 continue
#         return None
    
#     for i in positions:
#         dfs(i)

#     return True if (n - 1) in result else False




# dp
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * n
    
    for i in range(n):
        if s[:i + 1] in wordDict:
            dp[i] = True
            


    for i in range(n):
        for j in range(i):
            if dp[j] == False:
                continue

            if dp[j] == True and s[j + 1: i + 1] in wordDict:
                dp[i] = True
                break
        




    return dp[n - 1]

    


    


    


wordBreak(None, "aaaaaaa", ["aaaa","aaa"])
