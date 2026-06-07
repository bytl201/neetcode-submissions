class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [0] * len(arr)

        for i in range(len(arr)):
            max_int = -1
   
            for j in range(i+1, len(arr)):
                max_int = max(max_int, arr[j])
            
            print(i)
            
            result[i] = max_int
            print(result)
            print()

        return result