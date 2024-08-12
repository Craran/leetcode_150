from typing import Dict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')

        ns, nt = len(s), len(pattern)
        if ns != nt:
            return False
        
        hs: Dict[str, str] = {}
        ht: Dict[str, str] = {}

        for i in range(ns):
            if s[i] not in hs and pattern[i] not in ht:
                hs[s[i]], ht[pattern[i]] = pattern[i], s[i]
            elif s[i] in hs and pattern[i] in ht:
                if hs[s[i]] != pattern[i] or ht[pattern[i]] != s[i]:
                    return False
            else:
                return False

        return True