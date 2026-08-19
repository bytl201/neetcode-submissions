class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        diff = (arr[-1] - arr[0]) // len(arr)

        left, right = 0, len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[0] + middle * diff == arr[middle]:
                left = middle + 1

            else:
                right = middle - 1


        return arr[0] + left * diff