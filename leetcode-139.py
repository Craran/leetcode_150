from typing import List

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)
    words = {}
    positions = {}
    for word in wordDict:
        if word not in words:
            words[word] = len(word)
    
    for i in range(n):
        if s[:i + 1] in words:
            positions[i] = True

    


# wordBreak(None, "aaaaaaa", ["aaaa","aaa"])