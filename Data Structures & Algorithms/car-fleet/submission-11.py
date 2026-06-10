class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_list = [(p,s) for p,s in zip(position,speed)]
        p_list.sort()

        stack = []
        for p,s in p_list[::-1]:
            slope = (target - p) / s
            stack.append(slope)
            if len(stack)>= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
