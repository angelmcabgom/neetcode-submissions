class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] # pointer 1 
        max_profit = 0

        for price in prices[1:]: # pointer 2
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit