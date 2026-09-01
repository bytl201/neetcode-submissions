class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivotIndex, total_sum = -1, sum(nums)

        for i in range(len(nums)):
            pivotIndex = self.sumPivot(i, nums, total_sum)

            if pivotIndex != -1:
                break

        return pivotIndex

    def sumPivot(self, pivotIndex, nums, total_sum):
        left_sum, right_sum = 0, 0

        # calculate left total
        for i in range(pivotIndex):
            left_sum += nums[i]

        # calculate right total
        right_sum = (total_sum - left_sum) - nums[pivotIndex]

        return pivotIndex if left_sum == right_sum else -1
