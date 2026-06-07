class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_left = 0
        outer_right = len(matrix) - 1

        inner_list = []

        while outer_left <= outer_right:
            middle = outer_left + ((outer_right - outer_left) // 2)

            if matrix[middle][0] > target and matrix[middle][len(matrix[middle])-1] > target:
                outer_right = middle - 1
            elif matrix[middle][0] < target and  matrix[middle][len(matrix[middle])-1] < target:
                outer_left = middle + 1
            else:
                inner_list = matrix[middle]
                break

        print(inner_list)
        
        left = 0
        right = len(inner_list) -1
        while left <= right:
            middle = left + ((right-left)//2)
            print(f"left = {inner_list[left]}, right = {inner_list[right]}, middle = {inner_list[middle]}")
            print(f"left = {left}, right = {right}, middle = {middle}")
            print()

            if inner_list[middle] > target:
                right = middle -1
            elif inner_list[middle] < target:
                left = middle + 1
            else:
                return True

        return False