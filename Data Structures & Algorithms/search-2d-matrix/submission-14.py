class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_left, outer_right = 0, len(matrix) - 1
        arr = []

        # find the array with target value inside
        while outer_left <= outer_right:
            print(outer_left, outer_right)
            middle = (outer_left + outer_right) // 2

            middle_arr = matrix[middle]

            if middle_arr[0] <= target <= middle_arr[len(middle_arr)-1]:
                arr = middle_arr
                break
            elif middle_arr[len(middle_arr)-1] < target:
                outer_left = middle + 1
            elif middle_arr[0] > target:
                outer_right = middle - 1

        # find the target value inside array
        left, right = 0, len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] == target:
                return True
            elif arr[middle] > target:
                right = middle - 1
            elif arr[middle] < target:
                left = middle + 1

        return False
        