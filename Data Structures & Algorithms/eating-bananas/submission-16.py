class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_val = right

        while left <= right:
            middle = (left + right) // 2

            total = 0
            for i in piles:
                total += math.ceil(i/middle)
            if total <= h:
                min_val = min(min_val, middle)
                right = middle - 1
            else:
                left = middle + 1
        return min_val
