class TimeMap:

    def __init__(self):
        self.stack = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
            self.stack[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.stack.get(key,[])
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left+right) // 2

            if arr[middle][1] <= timestamp:
                res = arr[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return res

