class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currset, subset, = [], []
        self.helper(subset, currset, nums, 0)
        return subset
    def helper(self, subset, currset, nums, index):
        if index >= len(nums):
            subset.append(currset.copy())
            return

        currset.append(nums[index])
        self.helper(subset, currset, nums, index+1)
        currset.pop()
        self.helper(subset, currset, nums, index+1)


