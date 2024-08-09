class Solution:
    def mySqrt(self, x: int) -> int:
        x_0 = 1.0
        x_n = x_0 + 0.0
        while True:
            x_np1 = x_n - (x_n * x_n - x) / (2 * x_n)
            if abs(x_np1 - x_n) < 1e-3:
                return int(x_np1)
            x_n = x_np1