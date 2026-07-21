class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        result = 0

        while left <= right:
            middle = (left + right) // 2

            coins = middle * (middle + 1) / 2

            if coins > n:
                right = middle - 1
            else:
                left = middle + 1
                result = max(result, middle)

        return result