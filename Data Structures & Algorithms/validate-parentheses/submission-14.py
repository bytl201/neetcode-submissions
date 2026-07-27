class Solution:
    def isValid(self, s: str) -> bool:
        operations = {']': '[', ')':'(', '}':'{'}
        stack = []

        for i in s:
            if i not in operations:
                stack.append(i)
            elif stack and stack[-1] == operations[i]:
                stack.pop()
            else:
                return False

        return len(stack) == 0