from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(str(''.join(list(map(str, digits))))) + 1
        return list(map(int, list(str(s))))