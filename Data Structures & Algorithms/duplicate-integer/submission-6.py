class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}

        for i in nums:
            if i not in nums_dict.keys():
                nums_dict[i] = 1
            else:
                return True
            
        return False