def maxProfil(prices):
    n = len(prices)
    if n == 0:
        return 0
    dp = [0] * n
    minprice = prices[0]

    for i in range(1, n):
        minprice = min(minprice, prices[i])
        dp[i] = max(dp[i-1], prices[i] - minprice)
    return dp[-1]

prices = [7, 1, 5, 3, 6, 4]
maxprice = maxProfil(prices)
print(maxprice)