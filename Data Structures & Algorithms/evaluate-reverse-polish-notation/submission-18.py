class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}

        for i in tokens:
            if i in operations and len(stack) >= 2:
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
            else:
                stack.append(i)

        return int(stack[-1])
