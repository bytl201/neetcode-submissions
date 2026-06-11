class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []

        for i in range(len(arr)):
            maxx = 0
            for j in range(i+1, len(arr)):
                maxx = max(maxx, arr[j])
            
            res.append(maxx)
        res[-1] = -1
        return res