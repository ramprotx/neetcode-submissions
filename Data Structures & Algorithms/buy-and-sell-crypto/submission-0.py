class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        'buy low sell high'
        buy=999999        
        max_profit=0        
        for i in prices:
            if i < buy:
                buy = i
            elif i - buy > max_profit:
                max_profit = i - buy
        return max_profit