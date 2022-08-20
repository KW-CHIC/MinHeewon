# 주식을 사고팔기 가장 좋은 시점 (p.195)

import sys

def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 경신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

res = maxProfit([7, 1, 5, 3, 6, 4])
print(res)
