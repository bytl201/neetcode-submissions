class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                stackIndex, stackValue = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([i,v])
        return res

        