class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # index, temperature
        res = [0] * len(temperatures)

        for index, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append([index, t])

        return res