from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ss in s:
            if ss in brackets:
                stack.append(ss)
                continue
            if not stack:
                return False
            if ss == brackets[stack[-1]]:
                stack.pop()
                continue
            return False
        return True if not stack else False