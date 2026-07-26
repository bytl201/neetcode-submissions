class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        freq=[[] for i in range(len(nums)+1)]
        for key,val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                if len(res) == k:
                    break
                res.append(j)
        return res