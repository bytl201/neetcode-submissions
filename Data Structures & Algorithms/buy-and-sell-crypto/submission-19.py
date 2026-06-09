class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        maxP = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            right += 1
        return maxP