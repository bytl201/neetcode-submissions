class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            last = 0
            for i in range(len(self.queue)):
                last = i
            last_num = self.queue[last]
            self.queue = self.queue[:last]
            return last_num


    def top(self) -> int:
        last = 0
        for i in self.queue:
            last = i
        return last
    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()