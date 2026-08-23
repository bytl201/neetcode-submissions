class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset, currset = [], []
        self.helper(0, nums, subset, currset)
        return subset

    def helper(self, index, nums, subset, currset):
        if index == len(nums):
            subset.append(currset.copy())
            return
        
        currset.append(nums[index])
        self.helper(index+1, nums, subset, currset)
        currset.pop()

        while index + 1 < len(nums) and nums[index] == nums[index+1]:
            index += 1
        self.helper(index+1, nums, subset, currset)