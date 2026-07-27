class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i,v in enumerate(temperatures):

            while stack and stack[-1][1] < v:
                stackIndex, stackTemp = stack.pop()
                result[stackIndex] = i - stackIndex


            stack.append([i,v])

        return result