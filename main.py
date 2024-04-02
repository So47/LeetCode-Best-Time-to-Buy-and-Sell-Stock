class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # min_price = float('inf')

        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)
        # return max_profit

        # min_price = float('inf')  # Initialize min price as infinity
        # max_profit = 0  # Maximum profit initialized to 0
    
        # for price in prices:
        #     # If the current price is less than the minimum price seen so far, update min_price
        #     if price < min_price:
        #         min_price = price
        #     # Otherwise, calculate the profit if we were to sell at the current price
        #     # Update max_profit if this profit is greater than the current max_profit
        #     else:
        #         max_profit = max(max_profit, price - min_price)
                
        # return max_profit

        # Using two pointers , l for buy and r to sell
        # l, r = 0, 1
        # max_profit = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #        max_profit = max(max_profit, prices[r]-prices[l])
        #     else:
        #         l = r
        #     r +=1   

        # return max_profit

        # Using Sliding window
        l = 0
        max_profit = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r        

        return max_profit

