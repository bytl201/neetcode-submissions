class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for i in nums:
            if i -1 not in nums:
                length = 0
                while length + i in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest