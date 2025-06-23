prices = [7,2,5,1,8,4]

l = 0
r = 1
maxProfit = 0

while r < len(prices):
    # profitable 
    if prices[l] < prices[r]:
        profit = profit[r] - profit[l]
        maxProfit = max(maxProfit, profit)
    else:
        l = r 
    r += 1

