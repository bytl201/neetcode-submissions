class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []

        def helper(open_parantheses, close_parantheses):
            if n == open_parantheses == close_parantheses:
                res.append("".join(curr.copy()))
                return
            
            if open_parantheses < n:
                curr.append("(")
                helper(open_parantheses + 1, close_parantheses)
                curr.pop()

            if close_parantheses < open_parantheses:
                curr.append(")")
                helper(open_parantheses, close_parantheses + 1)
                curr.pop()

        helper(0,0)
        return res