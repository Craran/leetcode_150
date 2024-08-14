from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ls: List[str] = []
        n = len(strs[0])

        for i in range(n):
            ss = strs[0][i]
            for string in strs[1:]:
                if i >= len(string):
                    return ''.join(ls)
                if ss != string[i]:
                    return ''.join(ls)
                else:
                    continue
            ls.append(ss)
        return ''.join(ls)
