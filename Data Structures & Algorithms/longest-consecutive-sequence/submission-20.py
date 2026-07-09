class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        numbers = set(nums)

        for i in nums:
            if i -1 not in numbers:
                length = 0
                while length + i in numbers:
                    length += 1
                
                longest = max(longest, length)

        return longest