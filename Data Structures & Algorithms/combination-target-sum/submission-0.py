class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, currset, total_sum):

            if total_sum == target:
                res.append(currset.copy())
                return

            if index >= len(nums) or total_sum > target:
                return

            currset.append(nums[index])
            dfs(index, currset, total_sum + nums[index])
            currset.pop()
            dfs(index + 1, currset, total_sum)

        dfs(0, [], 0)
        return res
