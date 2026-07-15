class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_index = {}

        for i, v in enumerate(nums2):
            val_index[v] = i

        result = [0] * len(nums1)
        for i in range(len(nums1)):
            result[i] = val_index[nums1[i]]
        return result