from typing import List, Dict
class Solution:
    def get_nums(self, n: int) -> List:
        result = []
        while n > 0:
            result.append(n % 10)
            n //= 10
        return result

    def isHappy(self, n: int) -> bool:
        ht: Dict[int, bool] = {}
        now = n
        while True:
            
            nn = sum(map(lambda x: x ** 2, self.get_nums(now)))
            if nn == 1:
                return True
            if nn not in ht:
                ht[nn] = True
            else:
                return False
            now = nn
            