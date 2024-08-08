from typing import List

class Solution:
    # @staticmethod
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash_table = {}

        for i, s in enumerate(strs):
            sorted_str = str(sorted(s))
            if sorted_str in hash_table:
                hash_table[sorted_str].append(s)
            else:
                hash_table[sorted_str] = []
                hash_table[sorted_str].append(s)

        for val in hash_table.values():
            result.append(val)
            
        return result