class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        result = -1

        for n, o in count.items():
            if o == 1:
                result = max(result, n)
        return result