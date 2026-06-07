class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        freq =[[] for i in range (len(nums)+1)]

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        for index, value in hash_map.items():
            freq[value].append(index)

        result = []

        
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                result.append(freq[i][j])
                if len(result) == k:
                    return result
