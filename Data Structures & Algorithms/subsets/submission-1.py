class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, currset = [], []
        self.helper(0, nums, subset, currset)
        return subset
    def helper(self, index, nums, subset, currset):
        if index >= len(nums):
            subset.append(currset.copy())
            return

        currset.append(nums[index])
        self.helper(index+1, nums, subset, currset)

        currset.pop()
        self.helper(index+1, nums, subset, currset)

        return subset
