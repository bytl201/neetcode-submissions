class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination, current = [], []
        self.helper(0, 0,combination, current, nums, target)
        return combination

    def helper(self, index, total, combination, current, nums, target):
        if target == total:
            combination.append(current.copy())
            return

        if total > target or index >= len(nums):
            return
        
        current.append(nums[index])
        self.helper(index, total+nums[index], combination, current, nums, target)
        current.pop()
        self.helper(index+1, total, combination, current, nums, target)
        