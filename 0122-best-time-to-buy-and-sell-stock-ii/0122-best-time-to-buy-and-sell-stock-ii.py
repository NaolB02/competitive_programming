class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        summ = 0        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            summ += diff if diff > 0 else 0
        
        return summ