from typing import Dict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if ns != nt:
            return False
        # hs: Dict[str, int] = {}
        ht: Dict[str, int] = {}
        for ss, tt in zip(s, t):
            if ss not in ht:
                ht[ss] = 1
            else:
                ht[ss] += 1
            if tt not in ht:
                ht[tt] = -1
            else:
                ht[tt] -= 1

        for value in ht.values():
            if value != 0:
                return False
            
        return True
    
    """
    稍微有点儿不一样的思路，s字符串里的字符对应动作为数量+1，
    t字符串里的字符对应动作为数量-1
    最后看每个字符的结果对应的数量是不是都为0
    
    """
