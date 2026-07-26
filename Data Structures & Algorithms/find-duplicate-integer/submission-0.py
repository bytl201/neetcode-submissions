class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()
        for i in nums:
            if i not in unique:
                unique.add(i)
            else:
                return i