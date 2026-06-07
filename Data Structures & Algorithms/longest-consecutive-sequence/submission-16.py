class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i]-1 not in num_set:
                count = 0
                while nums[i] + count in num_set:
                    count += 1
                longest = max(longest,count)
            

        return longest