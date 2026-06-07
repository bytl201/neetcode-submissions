class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            value_count[i] = value_count.get(i, 0) + 1

        for index, value in value_count.items():
            freq[value].append(index)

        result = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if (len(result) == k):
                    return result
