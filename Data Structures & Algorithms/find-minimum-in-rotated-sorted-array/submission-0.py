class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]

        for i in nums:
            min_val = min(min_val, i)

        return min_val