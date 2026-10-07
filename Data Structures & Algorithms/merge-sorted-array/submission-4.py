class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last1, last2 = m-1, n-1
        i = len(nums1) - 1

        while last1 >= 0 and last2 >= 0 and i >= 0:
            if nums1[last1] < nums2[last2]:
                nums1[i] = nums2[last2]
                last2 -= 1
            else:
                nums1[i] = nums1[last1]
                last1 -= 1
            i -= 1

        while last2 >= 0:
            nums1[i] = nums2[last2]
            last2 -= 1
            i -= 1
