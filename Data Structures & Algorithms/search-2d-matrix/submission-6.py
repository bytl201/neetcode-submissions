class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        out_left = 0
        out_right = len(matrix) - 1
        out_list = []

        while out_left <= out_right:
            middle = (out_left + out_right) // 2
            if matrix[middle][0] < target and matrix[middle][len(matrix[middle])-1] < target:
                out_left = middle + 1
            elif matrix[middle][0] > target:
                out_right = middle - 1
            else:
                out_list = matrix[middle]
                break
        left = 0
        right = len(out_list) - 1

        while left <= right:
            middle = (left + right) // 2

            if out_list[middle] < target:
                left = middle + 1
            elif out_list[middle] > target:
                right = middle - 1
            else:
                return True
        return False