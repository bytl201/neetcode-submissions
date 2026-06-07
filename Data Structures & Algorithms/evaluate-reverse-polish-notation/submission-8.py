class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {'*', '/', '+', '-'}

        for i in tokens:

            if i not in operations or len(stack) < 2:
                stack.append(i)
            else:
                first_num = int(stack[-2])
                second_num = int(stack[-1])
                
                stack.pop()
                stack.pop()

                if i == "*":
                    stack.append(first_num*second_num)
                elif i == "/":
                    stack.append(int(first_num/second_num))
                elif i == "+":
                    stack.append(first_num+second_num)
                else:
                    stack.append(first_num-second_num)
        return int(stack[-1])