from typing import List

def maxProfit(self, prices: List[int]) -> int:
    result = 0
    min_array = [100005 for _ in range(len(prices))] # 0 ~ i
    max_array = [0 for _ in range(len(prices))] # i ~ n-1
    

    min_val = 100005
    max_val = 0
    
    for i in range(0, len(prices)):
        if prices[i] < min_val:
            min_val = min_array[i] = prices[i]
        else:
            min_array[i] = min_val

    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > max_val:
            max_val = max_array[i] = prices[i]
        else:
            max_array[i] = max_val

    for i in range(0, len(prices) - 1):
        result = max(max_array[i + 1] - min_array[i], result)
    return result