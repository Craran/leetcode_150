from typing import List


def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0    
    
    max_num = int(2 ** 31)

    dp = [-1] * (amount + 5)
    # cs = {}

    # for coin in coins:
    #     if coin in cs:
    #         continue
    #     cs[coin] = True
    
    # coins[:] = reversed(sorted(coins))
    for i in range(amount + 1):
        if i in coins:
            dp[i] = 1

    

    for i in range(amount + 1):
        if dp[i] == 1:
            continue
        min_sub = max_num
        for coin in coins:
            if i - coin < 1 or dp[i - coin] == -1:
                continue
            min_sub = min(min_sub, dp[i -coin])
        dp[i] = min_sub + 1 if min_sub != max_num else dp[i]
    return dp[amount] 

coinChange(None, [1,2,5], 11)