class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)

        longest = 0

        for i in nums:
            if i-1 not in nums:
                length = 0
                while i + length in num:
                    length += 1
                longest = max(longest, length)
        
        return longest