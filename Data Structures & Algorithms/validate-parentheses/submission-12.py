class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parentheses = {'}': '{', ')':'(', ']':'['}

        for i in s:
            if i not in parentheses:
                stack.append(i)
            else:
                if stack and stack[-1] == parentheses[i]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

