class Solution:
    def get_int(self, s: str) -> int:
        if s == 'I':
            return 1
        if s == 'V':
            return 5
        if s == 'X':
            return 10
        if s == 'L':
            return 50
        if s == 'C':
            return 100
        if s == 'D':
            return 500
        if s == 'M':
            return 1000
        return -0x3f3f3f3f
        
        
        
        
        
        

    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        
        sum = self.get_int(s[0])

        for i in range(1, len(s)):
            val = self.get_int(s[i])
            
            if (s[i] == 'V' or s[i] == 'X') and s[i - 1] == 'I':
                sum += val
                sum = sum - 2 * self.get_int('I')
            elif (s[i] == 'L' or s[i] == 'C') and s[i - 1] == 'X':
                sum += val
                sum = sum - 2 * self.get_int('I')
            elif (s[i] == 'D' or s[i] == 'M') and s[i - 1] == 'C':
                sum += val
                sum = sum - 2 * self.get_int('I')
            else:
                sum += val
        
        return sum