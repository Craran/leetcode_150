from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i, x in enumerate(temperatures):
            
            while len(st) > 0 and x > st[-1][1]:
                ans[st[-1][0]] = i - st[-1][0]
                st.pop()
                
            if len(st) == 0 or x <= st[-1][1]:
                st.append([i, x])

                
                
                
                
            
        while len(st) > 0:
            ans[st[-1][0]] = 0
            st.pop()

        return ans





