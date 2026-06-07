class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        longest = 0

        for i in nums:
            if not i-1 in all_nums:

                streak = 0

                while i + streak in all_nums:
                    streak +=1

                longest = max(longest, streak)

        return longest