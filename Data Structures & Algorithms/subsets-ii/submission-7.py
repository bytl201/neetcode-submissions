class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []
        self.helper(res, subset, nums, 0)
        return res

    def helper(self, res, subset, nums, index):
        if index >= len(nums) or len(subset) == len(nums):
            res.append(subset.copy())
            return

        num = nums[index]
        subset.append(num)
        self.helper(res, subset, nums, index+1)
        subset.pop()
        while index < len(nums) - 1 and nums[index] == nums[index+1]:
            index+= 1
        self.helper(res, subset, nums, index+1)