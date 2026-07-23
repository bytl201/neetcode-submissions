class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        arr = self.map.get(key, [])

        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle][1] <= timestamp:
                result = arr[middle][0]
                left = middle + 1
            else:
                right = middle - 1

        return result
        
