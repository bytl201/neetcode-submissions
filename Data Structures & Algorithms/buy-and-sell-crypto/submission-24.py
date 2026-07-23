class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left, right = 0, 1
        
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxP = max(profit, maxP)
            
            right += 1
        return maxP