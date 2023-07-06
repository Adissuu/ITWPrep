# Best Time to Buy and Sell Stock

### You are given an array prices where prices[i] is the price of a given stock on the ith day.

### You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

### Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

```
class Solution(object):
    def maxProfit(self, prices):
        buy, sell, profit = 0, 1, 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                curr = prices[sell] - prices[buy]
                profit = max(profit, curr)
            else:
                buy = sell 
            sell += 1
        return profit
```

#### If the sell price is higher than the buy price, do the actual calculation, else it means that we found a lower price, and it will be the new buy. Move the sell anyways.