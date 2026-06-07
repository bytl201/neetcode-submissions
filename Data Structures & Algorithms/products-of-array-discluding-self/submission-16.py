class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = [0] * len(nums)
        postfix_list = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prefix_list[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            postfix_list[i] = postfix
            postfix *= nums[i]

        res = [0] * len(nums)
        for i in range(len(nums)):
            index = postfix_list[i] * prefix_list[i]
            res[i] = index
        return res