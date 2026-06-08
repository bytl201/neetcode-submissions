class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)

        left = 0
        right = k - 1

        mini = nums[len(nums)-1]

        while right < len(nums):
            print(nums[left],nums[right],end="\n\n")

            diff = nums[right] - nums[left]
            mini = min(mini, diff)

            left += 1
            right += 1
        return mini