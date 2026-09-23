class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, perm = [], []
        candidates.sort()
        self.helper(res, perm, candidates, target, 0, 0)
        return res

    def helper(self, res, perm, candidates, target, total, index):
        if total == target:
            res.append(perm.copy())
            return
        elif total > target or index >= len(candidates):
            return
        else:
            num = candidates[index]
    
            perm.append(num)
            self.helper(res, perm, candidates, target, total+num, index+1)
            perm.pop()
            while index < len(candidates) -1  and num == candidates[index+1]:
                index+=1
            self.helper(res, perm, candidates, target, total, index+1)