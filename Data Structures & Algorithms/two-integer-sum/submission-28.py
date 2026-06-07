class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_nums = set(nums)

        count = {}

        for i in range(len(nums)):
            left_over = target - nums[i]

            if left_over in count.keys():
                return [count[left_over], i]

            count[nums[i]] = i