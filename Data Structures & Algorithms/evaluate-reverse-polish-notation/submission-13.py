class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operation = {'+', '-', '*', '/'}

        for i in tokens:
            if len(stack) >= 2 and i in operation:
                first_num = int(stack[-2])
                second_num = int(stack[-1])

                stack.pop()
                stack.pop()

                if i == "+":
                    stack.append(first_num + second_num)
                elif i == "-":
                    stack.append(first_num - second_num)
                elif i == "*":
                    stack.append(first_num * second_num)
                elif i == "/":
                    stack.append(int(first_num/second_num))

            else:
                stack.append(i)

        return int(stack[-1])