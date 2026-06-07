class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        
        left = 1

        res = max_val

        while left <= max_val:
            middle = (left + max_val) // 2

            total = 0
            for i in piles:
                total += math.ceil(i/middle)

            if total <= h:
                res = middle
                max_val = middle - 1
            elif total > h:
                left = middle + 1

        return res


        