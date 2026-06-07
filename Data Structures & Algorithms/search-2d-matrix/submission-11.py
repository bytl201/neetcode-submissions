class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        out_left = 0
        out_right = len(matrix) - 1

        arr = []
        while out_left <= out_right:
            middle = (out_left + out_right) // 2

            if matrix[middle][-1] < target:
                out_left = middle + 1
            elif matrix[middle][0] > target:
                out_right = middle - 1
            else:
                arr = matrix[middle]
                break

        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] > target:
                right = middle - 1
            elif arr[middle] < target:
                left = middle + 1
            else:
                return True

        return False