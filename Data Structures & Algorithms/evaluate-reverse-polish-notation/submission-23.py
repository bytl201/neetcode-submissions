class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+', '-', '*', '/'}
        result = 0
        stack = []

        for i in tokens:
            if i not in operations:
                stack.append(int(i))
                result = stack[-1]
            elif i == '+':
                addition = stack[-1] + stack[-2] 
                result = addition

                stack.pop()
                stack.pop()

                stack.append(addition)
            elif i == '-':
                subtraction = stack[-2] - stack[-1]
                result = subtraction

                stack.pop()
                stack.pop()
                stack.append(subtraction)
            
            elif i == '*':
                multiplication = stack[-1] * stack[-2]
                result = multiplication

                stack.pop()
                stack.pop()

                stack.append(multiplication)
            
            elif i == '/':
                division = int(stack[-2]/stack[-1])
                result = division

                stack.pop()
                stack.pop()

                stack.append(division)

        return result