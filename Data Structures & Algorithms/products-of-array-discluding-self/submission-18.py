class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        left_most = 1
        for i in range(len(nums)):
            res[i] = left_most 
            left_most *= nums[i]
        
        right_most = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= right_most
            right_most *= nums[i]

        return res