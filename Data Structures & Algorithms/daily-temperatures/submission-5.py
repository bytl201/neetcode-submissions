class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # index, temperature

        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append([index, value])

        return res
