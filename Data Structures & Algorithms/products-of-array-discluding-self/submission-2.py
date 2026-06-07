class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        prefix = [0] * len(nums)

        pre_count = 1
        for i in range(len(nums)):
            prefix[i] = pre_count
            pre_count *= nums[i]

        postfix = [0] * len(nums)
        post_count = 1
        for i in range (len(nums)-1, -1, -1):
            postfix[i] = post_count
            post_count *= nums[i]

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]

        return res