class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf')
        current_profit =0 
        for _ in prices :
            if _ <  min_price :
                min_price = _ 
            else :
                current_profit = _ - min_price
                if current_profit > max_profit :
                    max_profit = current_profit 
        return max_profit 
            
