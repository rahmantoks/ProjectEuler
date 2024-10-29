# Coin Sums
# There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# How many different ways can £2 be made using any number of coins]


def count(target):
    coins = [1,2,5,10,20,50,100,200]
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i-coin]
        
    return dp[target]

print(count(200))
