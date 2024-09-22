from typing import List

class Solution:
    # @staticmethod
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = n = 0
        length_1, length_2, length_3 = len(s1), len(s2), len(s3)
        if length_1 + length_2 != length_3:
            return False
        if length_1 == 0:
            return True if s2 == s3 else False
        if length_2 == 0:
            return True if s1 == s3 else False
        flag: bool = False
        i = j = k = 0

        while True:
            
            
            if flag == False:
                while i < length_1 and s1[i] == s3[k]:
                    i += 1
                    k += 1
                m += 1
                flag = True
            else:
                while j < length_2 and s2[j] == s3[k]:
                    j += 1
                    k += 1
                n += 1
                flag = False

            if k >= length_3:
                break
            
            if i == length_1 and j == length_2 and k == length_3:
                break
            elif i == length_1 and s2[j] != s3[k] or j == length_2 and s1[i] != s3[k]:
                return False
            elif i < length_1 and s1[i] != s3[k] and j < length_2 and s2[j] != s3[k]:
                return False
            
            
        
        return True

# a = Solution()
# print(a.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

# print(Solution.isInterleave(None, "aabcc", "dbbca", "aadbbcbcac"))