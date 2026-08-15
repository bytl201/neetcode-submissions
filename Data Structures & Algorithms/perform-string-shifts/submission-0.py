class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        arr_str = list(s)
        
        for d, a in shift:
            if d == 0:
                arr_str = self.shiftLeft(arr_str, a)

            else:
                arr_str = self.shiftRight(arr_str, a)

        sb = ""
        for i in arr_str:
            sb += i
        return sb
    def shiftRight(self, arr, amount):
        count = 0

        while count < amount:
            last_char = arr[-1]

            for i in range(len(arr)-1,0,-1):
                arr[i] = arr[i-1]

            arr[0] = last_char
            count += 1

        return arr

    def shiftLeft(self, arr, amount):
        count = 0

        while count < amount:
            first_char = arr[0]

            for i in range(1, len(arr)):
                arr[i-1] = arr[i]

            # a, b, c
            # b, b, c
            # b, c, c 

            arr[-1] = first_char
            count += 1

        return arr
        