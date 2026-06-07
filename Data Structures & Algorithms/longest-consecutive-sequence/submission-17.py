class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in nums:
            if i -1 not in num_set:
                maxi = 0
                while i + maxi in num_set:
                    maxi += 1
                longest = max(longest, maxi)

        return longest