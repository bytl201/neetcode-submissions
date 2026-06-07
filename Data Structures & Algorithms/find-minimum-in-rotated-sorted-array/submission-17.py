class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        min_val = nums[0]

        while left <= right:

            if nums[left] <= nums[right]:
                min_val = min(min_val, nums[left])
                break

            middle = (left + right) // 2
            min_val = min(min_val, nums[middle])

            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return min_val