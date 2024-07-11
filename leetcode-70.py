from typing import List

def climbStairs(self, n: int) -> int:
    f = [1] * (n + 5)
    f[2] = 2
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]
