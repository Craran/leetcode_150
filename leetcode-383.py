from typing import Dict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table: Dict[str, int] = {}
        for s in magazine:
            if s not in hash_table:
                hash_table[s] = 1
            else:
                hash_table[s] += 1


        for s in ransomNote:
            if s in hash_table and hash_table[s] > 0:
                hash_table[s] -= 1
            else:
                return False

        return True