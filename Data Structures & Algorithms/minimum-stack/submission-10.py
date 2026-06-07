class MinStack:

    def __init__(self):
        self.min_arr = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.min_arr:
            self.min_arr.append(min(self.min_arr[-1], val))
        else:
            self.min_arr.append(val)

        self.stack.append(val)
        

    def pop(self) -> None:
        self.min_arr.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
