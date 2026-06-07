class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while len(stack) >= 1 and t > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()

                res[stackIndex] = i - stackIndex

            else:
                stack.append([i,t])

        return res