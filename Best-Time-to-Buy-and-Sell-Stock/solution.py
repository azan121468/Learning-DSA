# idea is that we will keep track of minimum price so far
# if curr price is lower than minimum so far, we will update minimum so far
# but discard current price as we are all loss
# if this is not the case, then we will simply calcuate the profit and update 
# if greater than current profit

def maxProfit(prices):
    n = len(prices)

    min_sf = prices[0]
    max_profit = 0

    for i in range(1, n):
        if prices[i] < min_sf:
            min_sf = prices[i]
            continue        #we can use else instead but this is more understandable to me.
        
        profit = prices[i] - min_sf
        max_profit = max(max_profit, profit)
    
    return max_profit

profit = maxProfit([7,6,4,3,1])
print(profit)