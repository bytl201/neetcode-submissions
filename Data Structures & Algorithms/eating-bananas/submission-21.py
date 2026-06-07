class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        mini = right

        while left <= right:
            middle = (left + right) // 2

            hours = 0
            for i in piles:
                hours += math.ceil(i/middle)

            if hours <= h:
                mini = min(mini, middle)
                right = middle - 1
            else:
                left = middle + 1
            
        return mini