class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        arr = []

        while l<=r:

            middle = (l+r) // 2

            if matrix[middle][0] <= target <= matrix[middle][-1]:
                arr = matrix[middle]
                break
            elif matrix[middle][-1] > target:
                r = middle - 1
            else:
                l = middle + 1

        if len(arr) == 0:
            return False
        
        left = 0
        right = len(arr) -1 

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] == target:
                return True

            if arr[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False