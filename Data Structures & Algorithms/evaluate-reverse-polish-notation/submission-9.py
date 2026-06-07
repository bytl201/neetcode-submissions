class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}

        for i in tokens:
            if i in operations and len(stack) >=2:
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