class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = [[p,s] for p, s in zip(position,speed)]
        zipped.sort()
        stack = []

        for p,s in zipped[::-1]:
            slope = (target - p) / s
            stack.append(slope)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)