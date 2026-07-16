class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        result = [[] for i in range(len(nums)+1)]

        for n, o in count.items():
            result[o].append(n)
        
        if result[1]:
            return result[1][-1]
        else:
            return -1