class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        big = -1

        for i in range(len(arr)-1,-1,-1):
            res[i] = big
            big = max(big,arr[i])
        return res