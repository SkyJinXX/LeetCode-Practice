#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price = prices[0]
        for price in prices:
            if price < min_buy_price:
                min_buy_price = price
            else:
                max_profit = max(max_profit, price - min_buy_price)
        
        return max_profit
                

# @lc code=end

