class Solution:
    def countElements(self, arr: List[int]) -> int:
        unique = set(arr)
        counter = 0

        for i in arr:
            if i + 1 in unique: counter += 1

        return counter