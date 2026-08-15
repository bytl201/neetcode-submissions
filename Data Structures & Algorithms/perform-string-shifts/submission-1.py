class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net_shift = 0

        arr_str = list(s)

        for d, a in shift:
            net_shift += a if d == 1 else -a

        net_shift = net_shift % len(arr_str)

        arr_str = arr_str[-net_shift:] + arr_str[:-net_shift]

        return "".join(arr_str)