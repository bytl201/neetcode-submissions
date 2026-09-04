class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations, current = [], []
        self.helper(permutations, current, nums)
        return permutations
    
    def helper(self, permutations, current, nums):
        if len(current) == len(nums):
            permutations.append(current.copy())
            return

        for i in nums:
            if i not in current:
                current.append(i)

                self.helper(permutations, current, nums)

                current.pop()

        