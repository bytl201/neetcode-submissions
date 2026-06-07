class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        res = right

        while left <= right:

            middle = (left + right) // 2
            print(f"left = {left}, right = {right}, middle = {middle}")
            total = 0
            for i in piles:
                total += math.ceil(i/middle)
            print(f"total = {total}, res = {res}\n")

            if total <= h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1

        return res