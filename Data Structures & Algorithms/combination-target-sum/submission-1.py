class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def helper(index, currset, total):
            if total == target:
                res.append(currset.copy())
                return
            
            if index >= len(nums) or total > target:
                return

            currset.append(nums[index])
            helper(index, currset, total+nums[index])
            currset.pop()
            helper(index+1, currset, total)

        helper(0, [], 0)
        return res