class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb, current = [] , []
        self.helper(1, comb, current, n, k)
        return comb

    def helper(self, index, comb, current, n, k):       
        if len(current) == k:
            comb.append(current.copy())
            return
        if index > n:
            return 

        

        current.append(index)

        self.helper(index+1, comb, current, n, k)
        current.pop()
        self.helper(index+1, comb, current, n, k)

