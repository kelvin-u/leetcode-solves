prices = [7,2,5,1,8,4]

def maxProfit(prices):
    l = 0 
    r = 1
    maxP = 0 

    # sliding window apprach

    while r < len(prices):
        if prices[l] < prices[r]: # profitable
            profit =  prices[r] -  prices[l]
            maxP = max(maxP, profit)
        else: # not profitable price[l] >= price[r]
            l = r
        r += 1
    return maxP
