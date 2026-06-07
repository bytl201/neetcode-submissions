class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            left = target - nums[i]

            if left in nums_dict.keys():
                return [nums_dict[left], i]

            nums_dict[nums[i]] = i
        