class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for index, value in count.items():
            freq[value].append(index)

        result = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result