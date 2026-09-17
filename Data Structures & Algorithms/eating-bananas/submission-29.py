class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        mini = right

        while left <= right:
            middle = (left+right) // 2

            time = 0

            for i in piles:
                time += math.ceil(i/middle)
            
            if time <= h:
                mini = min(mini, middle)
                right = middle - 1
            else:
                left = middle + 1
        return mini