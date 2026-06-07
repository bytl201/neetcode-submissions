class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = count.get(i,0) + 1

        for key, value in count.items():
            freq[value].append(key)
        

        res = []

        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
                
