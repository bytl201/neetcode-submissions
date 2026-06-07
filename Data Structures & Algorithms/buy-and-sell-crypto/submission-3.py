class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                
                total = prices[j] - prices[i]

                if total > 0:
                    maxP = max(maxP, total)

        return maxP