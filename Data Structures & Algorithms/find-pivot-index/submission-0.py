class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivotIndex = -1

        for i in range(len(nums)):
            pivotIndex = self.sumPivot(i, nums)

            if pivotIndex != -1:
                break

        return pivotIndex

    def sumPivot(self, pivotIndex, nums):
        left_sum, right_sum = 0, 0

        # calculate left total
        for i in range(pivotIndex):
            left_sum += nums[i]

        # calculate right total
        for i in range(pivotIndex+1, len(nums)):
            right_sum += nums[i]

        return pivotIndex if left_sum == right_sum else -1
