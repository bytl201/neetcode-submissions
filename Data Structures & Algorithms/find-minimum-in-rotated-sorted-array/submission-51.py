class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mini = nums[right]

        while left <= right:
            middle = (left + right) // 2

            if nums[left] <= nums[right]:
                mini = min(mini,nums[left])
                break

            mini = min(mini, nums[middle])
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return mini