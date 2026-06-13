class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        print(left, right)

        mini = right

        while left <= right:
            middle = (left + right) // 2
            print(middle)
            total = 0
            for i in piles:
                total += math.ceil(i/middle)
            
            if total <= h:
                mini = min(mini, middle)
                right = middle - 1
            else:
                left = middle + 1

        return mini