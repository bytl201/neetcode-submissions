class Solution:
    def countElements(self, arr: List[int]) -> int:
        unique = set(arr)
        count = 0

        for i in arr:
            if i + 1 in unique:
                count += 1
        
        return count