class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i in range(len(nums)):

            left = target - nums[i]

            if left in count:
                return [count[left], i]
            count[nums[i]] = i