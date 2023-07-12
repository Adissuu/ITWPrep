class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        buy, sell, profit = 0, 1, 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                curr = prices[sell] - prices[buy]
                profit = max(profit, curr)
            else:
                buy = sell
            sell += 1
        return profit
