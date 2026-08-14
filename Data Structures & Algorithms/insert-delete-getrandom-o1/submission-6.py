class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.arr.append(val)
            self.map[val] = len(self.arr) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.map:
            index = self.map[val]
            last_value = self.arr[-1]
            self.arr[index] = last_value
            self.map[last_value] = index
            self.arr.pop()
            self.map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()