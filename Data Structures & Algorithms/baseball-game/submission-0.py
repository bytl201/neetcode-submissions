class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        operation = {'+', 'D', 'C'}

        for i in operations:
            if i not in operation:
                stack.append(int(i))
            elif i == '+' and len(stack)>=2:
                firstNum = int(stack[-2])
                secondNum = int(stack[-1])

                stack.append(firstNum+secondNum)
            elif i == 'D':
                stack.append(int(stack[-1] * 2))
            elif i == 'C':
                stack.pop()

        total = 0
        for i in stack:
            total += i
        return total