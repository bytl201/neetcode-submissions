class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # index value
        res = [0] * len(temperatures)

        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append([index,value])
        return res