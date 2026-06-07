class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            # Check if the left half [left...middle] is sorted
            if nums[left] <= nums[middle]:
                # If target is within the sorted left half
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # Otherwise, the right half [middle...right] must be sorted
            else:
                # If target is within the sorted right half
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1