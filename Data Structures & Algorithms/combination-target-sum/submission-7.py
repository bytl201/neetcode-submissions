class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        self.helper(res, curr, nums, target, 0, 0)
        return res

    def helper(self, res, curr, nums, target, total, index):
        if total > target or index == len(nums):
            return
            
        if total == target:
            res.append(curr.copy())
            return

        

        curr.append(nums[index])
        self.helper(res, curr, nums, target, total+nums[index], index)

        curr.pop()
        self.helper(res, curr, nums, target, total, index+1)
