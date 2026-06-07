class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_mapping = set()
        for i in nums:
            if i in nums_mapping:
                return True
            else:
                nums_mapping.add(i)
        return False