class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique = set(nums)

        for i in nums:

            if i - 1 not in unique:
                count = 0
                while count + i in unique:
                    count += 1

                longest = max(longest, count)


        return longest