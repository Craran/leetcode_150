class Solution:
    def romanToInt(self, s: str) -> int:
        ht = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        # label = [True for _ in range(len(s) + 5)]
        sum = 0

        for i in range(len(s) - 1):
            if ht[s[i]] >= ht[s[i + 1]]:
                sum += ht[s[i]]
            else:
                sum -= ht[s[i]]
        sum += ht[s[-1]]
        return sum