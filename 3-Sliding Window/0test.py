prices = [7,2,5,1,8,4]

# best time to buy and sell stock 
l = 0  # buy
r = 1  # sell
maxProfit = 0 

while r < len(prices):
    # profitable
    if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        maxProfit = max(maxProfit, profit)
    # not profitable higher buy price than sell price, dont buy
    else:
        l = r
    r+=1 
print(maxProfit)
        

