class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        string = ""
        arr = self.map[key]
        print(arr)

        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2

            if arr[middle][1] <= timestamp:
                string = arr[middle][0]
                left = middle + 1
            else:
                right -= 1

        return string
