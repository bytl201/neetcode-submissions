class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def helper(index, current, total_sum):

            if total_sum == target:
                res.append(current.copy())
                return

            if index >= len(nums) or total_sum > target:
                return

            current.append(nums[index])
            helper(index, current, total_sum+nums[index])

            current.pop()
            helper(index+1, current, total_sum)


        helper(0,[],0)
        return res