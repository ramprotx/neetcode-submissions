class Solution:
     def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

    # def maxProfit(self, prices: List[int]) -> int:
    #     maxP = 0
    #     minBuy = prices[0]

    #     for sell in prices:
    #         maxP = max(maxP, sell - minBuy)
    #         minBuy = min(minBuy, sell)
    #     return maxP

    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     for i in range(len(prices)):
    #         buy = prices[i]
    #         for j in range(i + 1, len(prices)):
    #             sell  = prices[j]
    #             res = max(res, sell - buy)
    #     return res

    # def maxProfit(self, prices: List[int]) -> int:
    #     'buy low sell high'
    #     buy=999999        
    #     max_profit=0        
    #     for i in prices:
    #         if i < buy:
    #             buy = i
    #         elif i - buy > max_profit:
    #             max_profit = i - buy
    #     return max_profit