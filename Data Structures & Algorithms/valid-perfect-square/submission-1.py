class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            middle = (left + right) // 2

            squared = middle * middle

            if squared > num:
                right = middle - 1
            elif squared < num:
                left = middle + 1
            else:
                return True

        
        return False