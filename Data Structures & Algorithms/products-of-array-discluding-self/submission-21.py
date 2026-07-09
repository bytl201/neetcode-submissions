class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            result[i] = left * result[i]
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] = right * result[i]
            right *= nums[i]

        return result
