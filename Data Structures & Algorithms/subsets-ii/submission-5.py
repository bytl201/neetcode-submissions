class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset, currset = [], []
        self.helper(nums, 0, subset, currset)
        return subset
    def helper(self, nums, index, subset, currset):
        if index >= len(nums):
            subset.append(currset.copy())
            return

        currset.append(nums[index])
        self.helper(nums, index+1, subset, currset)
        currset.pop()

        while index+1 < len(nums) and nums[index] == nums[index+1]:
            index += 1

        self.helper(nums, index+1, subset, currset)