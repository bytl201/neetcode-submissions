class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_mapping = {}
        for i in nums:
            if i in nums_mapping.keys():
                return True
            else:
                nums_mapping[i] = 1
        return False