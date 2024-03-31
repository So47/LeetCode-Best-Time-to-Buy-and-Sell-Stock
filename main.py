class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # min_price = float('inf')

        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)
        # return max_profit

        # Using two pointers , l for buy and r to sell
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
               max_profit = max(max_profit, prices[r]-prices[l])
            else:
                l = r
            r +=1   

        return max_profit
