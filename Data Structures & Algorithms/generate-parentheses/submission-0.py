class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []

        def helper(opened, closed):
            if opened == closed == n:
                res.append("".join(curr))
                return 
            if opened < n:
                curr.append("(")
                helper(opened + 1, closed)
                curr.pop()
            if closed < opened:
                curr.append(")")
                helper(opened, closed + 1)
                curr.pop()
                
        helper(0, 0)

        return res
