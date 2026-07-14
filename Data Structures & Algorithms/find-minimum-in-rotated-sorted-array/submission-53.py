class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mini = nums[right]

        while left <= right:
            if nums[left] <= nums[right]:
                mini = min(mini, nums[left])
                break
            
            middle = (left + right) // 2
            mini = min(mini, nums[middle])

            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
            
            print(middle)

        return mini