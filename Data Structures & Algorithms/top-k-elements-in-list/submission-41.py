class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_list = [[] for i in range(len(nums)+1)]

        count = {}

        for i in nums:
            count[i] = count.get(i,0) + 1

        for key, val in count.items():
            res_list[val].append(key)

        res = []

        print(res_list)

        for i in range(len(res_list)-1,0,-1):
            for j in res_list[i]:
                res.append(j)
                if len(res) == k:
                    return res