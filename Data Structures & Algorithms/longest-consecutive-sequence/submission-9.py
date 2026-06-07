class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)

        streak = 0

        for i in nums:
            if i -1 not in all_nums:

                length = 0
                while i+length in all_nums:
                    length +=1

                streak = max(streak, length)

        return streak