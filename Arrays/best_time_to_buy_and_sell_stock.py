# LeetCode 121 - Best Time to Buy and Sell Stock

# Category: Array, Sliding Window

# Approach:
# Keep track of the minimum stock price seen so far.
# For each day's price, calculate the profit by subtracting the minimum
# price from the current price. Update the maximum profit if the current
# profit is greater. Also update the minimum price whenever a lower price
# is found.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
