class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0


        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            
            length = int(s[left:right])
            
            res.append(s[right + 1 : right + 1 + length])
            left = right + 1 + length

        return res