class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        for i in nums:
            if i not in num_dict.keys():
                num_dict[i] = 1
            else:
                return True
        return False