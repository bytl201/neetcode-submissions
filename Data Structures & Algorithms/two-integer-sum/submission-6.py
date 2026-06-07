class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, value in enumerate(nums):

            remainder = target - value

            if remainder in nums_dict.keys():
                return [nums_dict[remainder], index]

            nums_dict[value] = index