class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+', '-', '*', '/'}
        stack = []

        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                firstNum = int(stack[-2])
                secondNum = int(stack[-1])

                stack.pop()
                stack.pop()

                if i == '+':
                    stack.append(firstNum + secondNum)
                elif i == '-':
                    stack.append(firstNum - secondNum)
                elif i == '*':
                    stack.append(firstNum * secondNum)
                elif i == '/':
                    stack.append(int(firstNum/secondNum))
        return int(stack[-1])
