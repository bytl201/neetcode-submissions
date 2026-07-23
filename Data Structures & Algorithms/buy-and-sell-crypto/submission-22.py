class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window = set()
        maxP = 0

        left = prices[0]
        for right in prices:
            if left >= right:
                left = right
            else:
                profit = right - left
                maxP = max(maxP, profit)

        return maxP