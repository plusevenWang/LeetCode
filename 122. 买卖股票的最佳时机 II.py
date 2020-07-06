def maxProfit(prices: [int]) -> int:
    profit = 0
    for i in range(1,len(prices)):
        diff = prices[i] - prices[i-1]
        if diff > 0:
            profit += diff
    return profit


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(maxProfit(prices))
