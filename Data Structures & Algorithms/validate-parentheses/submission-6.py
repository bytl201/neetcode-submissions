class Solution:
    def isValid(self, s: str) -> bool:
        closeParentheses = {'}':'{', ')':'(', ']':'['}
        stack = []

        for i in s:
            if i in closeParentheses.keys():
                if stack and stack[-1] == closeParentheses[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)

        return True if len(stack) == 0 else False