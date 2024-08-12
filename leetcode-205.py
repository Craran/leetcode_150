from typing import Dict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if ns != nt:
            return False
        
        hs: Dict[str, str] = {}
        ht: Dict[str, str] = {}

        for i in range(ns):
            if s[i] not in hs and t[i] not in ht:
                hs[s[i]], ht[t[i]] = t[i], s[i]
            elif s[i] in hs and t[i] in ht:
                if hs[s[i]] != t[i] or ht[t[i]] != s[i]:
                    return False
            else:
                return False

        return True