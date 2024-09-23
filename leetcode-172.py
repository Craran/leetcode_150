class Solution:
    def trailingZeroes(self, n: int) -> int:
        

        cnt = 0
        cnt_2, cnt_5 = 0, 0
        for i in range(1, n + 1):
            now = i
            
            while now % 5 == 0:
                cnt_5 += 1
                now //= 5
            while now % 2 == 0:
                cnt_2 += 1
                now //= 2
        
        cnt = min(cnt_2, cnt_5)
        return cnt
        
        
        