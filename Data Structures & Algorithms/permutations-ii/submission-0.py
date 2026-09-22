class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {n:0 for n in nums}
        for i in nums:
            count[i] += 1

        def dfs():
            for num in count.keys():
                if len(perm) == len(nums):
                    res.append(perm.copy())
                    return

                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1

                    dfs()

                    perm.pop()
                    count[num] += 1

        dfs()
        return res
