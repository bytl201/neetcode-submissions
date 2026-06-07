class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = arr[-1]
        for i in range(len(arr)-2 , -1 ,-1 ): 
            arr[i] , right_max =  right_max, max(right_max,arr[i])
        arr[-1] = -1
        return arr 