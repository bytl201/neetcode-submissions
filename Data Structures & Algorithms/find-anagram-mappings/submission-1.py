class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [0] * len(nums1)

        for i in range(len(nums1)):
            left = 0
            right = len(nums1) - 1

            while left <= right:
                print(f"Num: {nums1[i]}, left = {nums2[left]}, right = {nums2[right]}")
                if nums2[left] == nums1[i]:
                    result[i] = left
                    break
                elif nums2[right] == nums1[i]:
                    result[i] = right
                    break
                
                left += 1
                right -= 1
            print()
        return result