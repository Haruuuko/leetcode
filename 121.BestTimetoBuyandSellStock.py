'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = sell = prices[0]
        profit = 0
        for i in prices:
            if i > sell:
                sell = i
                if sell - buy > profit:
                    profit = sell - buy
            elif i < buy:
                sell = buy = i
        return profit

print(Solution().maxProfit([6,2,5,4,1,6]))
