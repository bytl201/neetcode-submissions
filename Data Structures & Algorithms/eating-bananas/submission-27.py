class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = max(piles)
        left, right = 1, mini

        while left <= right:
            middle = (left + right) // 2

            result = 0
            for i in piles:
                result += math.ceil(i / middle)

            if result <= h:
                mini = middle
                right = middle - 1
            else:
                left = middle + 1

        return mini