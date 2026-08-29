class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currset, subset = [], []
        self.helper(0, nums, currset, subset)
        return subset
    

    def helper(self, index, nums, currset, subset):
        if index == len(nums):
            subset.append(currset.copy())
            return

        currset.append(nums[index])
        self.helper(index+1, nums, currset, subset)
        while index+1 < len(nums) and nums[index] == nums[index+1]:
            index+=1

        currset.pop()
        self.helper(index+1, nums, currset, subset)


        
