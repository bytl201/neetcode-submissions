class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result+= str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1

            length = int(s[left:right])
            print(s[right+1:right+length+1])

            result.append(s[right+1:right+length+1])

            left = right+ length + 1
        return result